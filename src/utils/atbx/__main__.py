import argparse
import pathlib
import re
import zipfile

# from . import get_tb_info

# logging.basicConfig(level=logging.DEBUG)


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("operation")
    args = arg_parser.parse_args()

    # Extract the files from the atbx zip archive
    if re.search("extract", args.operation, re.IGNORECASE):
        for atbx in pathlib.Path(".").glob("**/*.atbx"):
            # get_tb_info(atbx)
            print(atbx)
            with zipfile.ZipFile(atbx, "r") as atbx_zip:
                atbx_zip.extractall(atbx.with_suffix(".atbx.extracted"))
    else:
        # Create a new atbx file
        for atbx_dir in pathlib.Path(".").glob("**/*.atbx.extracted"):
            if not atbx_dir.is_dir():
                continue

            atbx_name = atbx_dir.with_suffix("")
            print(f"Now adding files from {atbx_dir} into {atbx_name}...")
            with zipfile.ZipFile(atbx_name, "w") as atbx_zip:
                for tb_item_path in atbx_dir.glob("**/*"):
                    arc_name = tb_item_path.relative_to(atbx_dir)
                    print(f"Writing {tb_item_path} to {atbx_name}")
                    atbx_zip.write(tb_item_path, arc_name)


if __name__ == "__main__":
    main()
