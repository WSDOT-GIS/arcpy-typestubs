"""Generates a list of all currently loaded Geoprocessing 
tools and their parameters.
"""
import argparse
import logging


# from itertools import groupby
from typing import Optional

from . import enumerate_tool_info

_LOGGER = logging.getLogger()
logging.basicConfig(filename="tool_dump.log", level=logging.DEBUG)


def main():
    # logger = _LOGGER.getChild(main.__name__)
    arg_parser = argparse.ArgumentParser(description=__doc__)
    arg_parser.add_argument("--wildcard", type=str, required=False, default=None)
    args = arg_parser.parse_args()

    tool_infos = enumerate_tool_info(args.wildcard)

    # Initialize variables for checking to see when the loop
    # has encountered a new toolbox or tool within a toolbox.
    current_toolbox: Optional[str] = None
    current_tool: Optional[str] = None
    for tool_info in tool_infos:
        (
            toolbox_name,
            toolbox_alias,
            tool_full_name,
            tool_name,
            parameter_properties,
        ) = tool_info
        if toolbox_name != current_toolbox:
            print(f"\n## {toolbox_name} ({toolbox_alias})\n")
            current_toolbox = toolbox_name
            # Reset tool
            current_tool = None
        if tool_full_name != current_tool:
            print(f"### {tool_name}\n")
            current_tool = tool_full_name
            print("#### Parameters\n")

            p_names = [p.name for p in parameter_properties]
            # Print table header names
            print(" | ".join(p_names))
            # Print column separators
            print("|".join(["-" * 5] * len(p_names)))
            
        p_values = [f'`{repr(p.value)}`' for p in parameter_properties]
        print("|".join(p_values))


if __name__ == "__main__":
    main()
