import argparse
from pathlib import Path
import logging
from sys import stderr

LOGGER = logging.getLogger()


def _create_dir(d: Path, dry_run: bool):
    logger = LOGGER.getChild(_create_dir.__name__)
    if d.exists():
        exists_msg = f'Directory already exists: "{d.absolute()}"'
        stderr.writelines(("\n", exists_msg))
        logger.info(exists_msg)
    elif dry_run:
        print(f"Would have created {d}")
    else:
        d.mkdir(parents=True, exist_ok=True)


def _create_file(init_path: Path, dry_run: bool):
    logger = LOGGER.getChild(_create_file.__name__)
    if init_path.exists():
        logger.info(f"File already exits: {init_path.absolute()}")
        return
    else:
        logger.info(f"File does not exist: {init_path.absolute()}")

    if dry_run:
        stderr.writelines(("\n", f"Would have created {init_path.absolute()}"))
    else:
        init_path.touch(exist_ok=True)


def create_gp_package_folders(module_name: str, root: Path, dry_run: bool = False):
    """Creates folder structure for ArcGIS Geoprocessing module project,
    as described in
    [Extend a Python package with geoprocessing tools](https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/extending-geoprocessing-through-python-modules.htm#ESRI_SECTION1_4E526239BD504D61979437D71A27FFC6)

    ```shell
    src
    └──<your module name>
        ├  __init__.py
        ├  bar.py
        └──esri
            ├──arcpy
            ├──help
            │   └──gp
            │       ├──messages
            │       └──toolboxes
            └──toolboxes
    ```

    Args:
        module_name (str): The name of your module
        root (pathlib.Path): The folder where the folders will be created.
        dry_run (bool): Report what WOULD'VE happened without actually making changes.
    """
    logger = LOGGER.getChild(create_gp_package_folders.__name__)

    if not root.exists() or not root.is_dir():
        msg = f'"{root}" either does not exist or is not a directory.'
        err = NotADirectoryError(msg)
        logger.exception(msg, exc_info=err)
        raise err

    # Create the package "src" folder.
    # All other files and directories created here
    # will be inside this folder.
    pk_root = root.joinpath("src", module_name)

    # Create paths for the new folders.
    new_dirs = (
        pk_root.joinpath(d)
        for d in (
            "esri/arcpy",
            "esri/help/gp/messages",
            "esri/help/gp/toolboxes",
            "esri/toolboxes",
        )
    )

    for d in new_dirs:
        _create_dir(d, dry_run)

    init_path = pk_root.joinpath("__init__.py")

    _create_file(init_path, dry_run)


def main():
    arg_parser = argparse.ArgumentParser(description=__doc__)
    arg_parser.add_argument("package_name", type=str)
    arg_parser.add_argument("root_dir", type=Path)
    arg_parser.add_argument("--dry-run", action="store_true")
    args = arg_parser.parse_args()

    create_gp_package_folders(args.package_name, args.root_dir, args.dry_run)


if __name__ == "__main__":
    main()
