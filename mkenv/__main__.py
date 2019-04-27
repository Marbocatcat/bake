#!/bin/env python3

import argparse

from mkenv import Mkenv
from .__init__ import __version__


def get_args():
    """Get script arguments."""
    description = "mkenv - automated dev environment."

    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("--filename", help="desired filename for project.")

    arg.add_argument("--version", action="store_true", help="print \"mkenv\" \
                    version.")

    return arg.parse_args()


def process_args(args):
    if args.version:
        print(f"mkenv {__version__}")
        exit(0)


def main():
    """Main script function."""
    args = get_args()
    process_args(args)

    try:
        create_env = Mkenv(args.filename)
        create_env._createProject()

    except TypeError as error:
        print(f"Please add a filename with: \"--filename\".")


if __name__ == '__main__':
    main()
