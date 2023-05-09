"""Scrapes GP service info
"""
import json
import logging
import re
from os import makedirs
from pathlib import Path
import sys
from typing import Any, Sequence, Union
from typing_extensions import Literal, TypedDict
import requests

SERVICE_NAME_RE = re.compile(
    r".+/arcgis/rest/services/(?P<name>([^\/]+/?){1,2})/GPServer", re.IGNORECASE
)

DEFAULT_PARAMS = {"f": "json"}

LOGGER = logging.getLogger()
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# class UrlFormatError(Exception):
#     def __init__(self):
#         super()

EsriExecutionType = Literal["esriExecutionTypeSynchronous"]
DataType = Literal["GPString"]
EsriGPParameterDirection = Literal[
    "esriGPParameterDirectionInput", "esriGPParameterDirectionOutput"
]
EsriGPParameterType = Literal["esriGPParameterTypeRequired"]


class ErrorResponseErrorDict(TypedDict):
    code: int
    message: str
    details: Sequence[Any]


class ErrorResponseDict(TypedDict):
    error: ErrorResponseErrorDict


class ServiceDict(TypedDict):
    currentVersion: float
    serviceDescription: str
    tasks: Sequence[str]
    executionType: EsriExecutionType
    resultMapServerName: str
    maximumRecords: int


class ParamDict(TypedDict):
    name: str
    dataType: DataType
    displayName: str
    description: str
    direction: EsriGPParameterDirection
    defaultValue: Union[str, float]
    parameterType: EsriGPParameterType
    category: str


class TaskDict(TypedDict):
    name: str
    displayName: str
    description: str
    category: str
    helpUrl: str  # HTML URL
    executionType: EsriExecutionType
    parameters: Sequence[ParamDict]


def get_service_name_from_url(url: str):
    logger = LOGGER.getChild(get_service_name_from_url.__qualname__)
    logger.debug("URL: %s", url)
    match = SERVICE_NAME_RE.match(url)
    logger.debug("match: %s", match)
    if not match:
        raise Exception("URL was not in expected format.")

    return match.group("name")


def get_task_info(url: str, task_name: str):
    logger = LOGGER.getChild(get_task_info.__qualname__)
    logger.debug("service url: %s", url)
    task_url = "/".join([url, task_name])  # url_parse.urljoin(url, task_name)
    logger.info("task url %s", task_url)
    response = requests.get(task_url, DEFAULT_PARAMS)
    info: Union[TaskDict, ErrorResponseErrorDict] = response.json()
    if "error" in info:
        raise Exception(f"An error occurred with {task_url}:\n {info}")
    return task_url, info


def get_task_infos(url: str, serviceInfo: ServiceDict):
    logger = LOGGER.getChild(get_task_infos.__qualname__)
    logger.debug("url: %s, service info: %s", url, serviceInfo)
    for task_name in serviceInfo["tasks"]:
        logger.debug("current task: %s", task_name)
        task_url, task_info = get_task_info(url, task_name)
        logger.debug("task info: %s", task_info)
        yield task_name, task_url, task_info


json_suffix = ".json"


def get_service_info(output_dir: Path, url: str):
    """Queries a map service to get information about it.

    Args:
        output_dir (Path): A directory that the output file name will be a child of.
        url (str): GP Service URL. Should end in GPServer

    Returns:
        A tuple of service info and a JSON file path.
        Note that this function does not create the JSON file.
    """
    with requests.get(url, DEFAULT_PARAMS) as response:
        info: ServiceDict = response.json()
        # json_path = output_dir.joinpath(info["name"])
        svc_name = get_service_name_from_url(url)
        json_path = output_dir.joinpath(*svc_name.split("/")).with_suffix(json_suffix)
        return info, json_path


def dump_service_info(service_urls: Sequence[str], output_dir: Union[Path, str]):
    path_open_args = {"encoding": "utf-8", "newline": "\n"}
    json_dump_args = {"indent": 2}

    if isinstance(output_dir, str):
        output_dir = Path(output_dir)
    # Create the output dir
    if not output_dir.exists():
        makedirs(output_dir)

    # Loop through the GP Service URLs
    for url in service_urls:
        info, json_path = get_service_info(output_dir, url)
        svc_parent_dir = json_path.parent
        makedirs(svc_parent_dir, exist_ok=True)
        svc_folder = json_path.with_suffix("")
        makedirs(svc_folder, exist_ok=True)
        with json_path.open("wt", **path_open_args) as f:
            json.dump(info, f, **json_dump_args)
        # Loop through the service's tasks
        for task_name, task_url, task_info in get_task_infos(url, info):
            task_path = svc_folder.joinpath(task_name).with_suffix(json_suffix)
            with task_path.open("wt", **path_open_args) as f:
                json.dump(task_info, f, **json_dump_args)

            # execute the task
            with requests.get(
                "/".join([task_url, "execute"]), DEFAULT_PARAMS
            ) as task_result:
                task_response = task_result.json()
                task_result_path = task_path.with_suffix(".result.json")
                with task_result_path.open("wt", **path_open_args) as f:
                    json.dump(task_response, f, **json_dump_args)
