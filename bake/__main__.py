#!/bin/env python3

import argparse

from bake import Bake
from .__init__ import __version__


def get_args():
    """Get script arguments."""

    description = "bake - automated dev environment creation."

    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("--cake", type=str, default="ERROR", help="desired filename for project.")

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

    if args.cake is "ERROR":
        print("Please add cake!")
        exit(0)

    if args.cake.isnumeric() is False:

        try:
            bake = Bake(args.cake)
            bake._create_cake()

        except TypeError as error:
            print(f"Please add a filename with: \"--cake\".")
    else:
        print("Cake can't be just integers.")


if __name__ == '__main__':
    main()
