import logging
from typing import Sequence
from typing_extensions import TypedDict
import zipfile

_LOGGER = logging.getLogger()


class ToolsetDict(TypedDict):
    # All items in tools end with ".tool"
    tools: Sequence[str]


class ToolboxContentDict(TypedDict):
    version: str  # "1.0"
    alias: str  # "sport"
    displayname: str  # "$rc:title"
    toolsets: Sequence[ToolsetDict]


def get_tb_info(atbx_file: str):
    logger = _LOGGER.getChild(get_tb_info.__qualname__)
    logger.debug("Toolbox file: %s", atbx_file)
    with zipfile.ZipFile(atbx_file) as atbx:
        for info in atbx.infolist():
            logger.debug("%s", info)
