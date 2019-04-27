#!/bin/env python3

import argparse

from bake import Bake
from .__init__ import __version__


def get_args():
    """Get script arguments."""
    description = "bake - automated dev environment."

    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("--cake", help="desired filename for project.")

    arg.add_argument("--version", action="store_true", help="print \"bake\" \
                    version.")

    return arg.parse_args()


def process_args(args):
    if args.version:
        print(f"bake {__version__}")
        exit(0)


def main():
    """Main script function."""
    args = get_args()
    process_args(args)

    try:
        create_env = Bake(args.cake)
        create_env._create_project()

    except TypeError as error:
        print(f"Please add a filename with: \"--cake\".")


if __name__ == '__main__':
    main()
