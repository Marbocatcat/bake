# mkenv

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md)

`mkenv` is a script that automates project creating in a LINUX environment. The script creates the following directory files:

- PROJECT\PROJECT\PROJECT.py
- PROJECT\README.md
- PROJECT\setup.py
- PROJECT\venv

It also installs Pythons virtualenv.

## Dependencies
None

## Installation

Clone the project.
```sh
pip3.7 install --editable .
```
in \mkenv directory.

## Usage

```sh
usage: mkenv [-h] [--filename FILENAME] [--version]

mkenv - automated dev environment.

optional arguments:
  -h, --help           show this help message and exit
  --filename FILENAME  desired filename for project.
  --version            print "mkenv" version.
```
