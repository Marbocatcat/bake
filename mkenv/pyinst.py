#!/bin/env python3

from mkenv import Mkenv
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", required=True)
    parser.add_argument("--mksetupfile", action="store_true")
    args = parser.parse_args()


    my_project = Mkenv(args.filename)
    my_project._createProject()


if __name__ == '__main__':
    main()
