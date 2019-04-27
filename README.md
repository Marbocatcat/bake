# bake 

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md)

`bake` is a script that automates project creation in a LINUX environment. The script creates the following directory files:

- CAKE\CAKE\cake.py
- CAKE\README.md
- CAKE\setup.py
- CAKE\venv

It also installs Pythons virtualenv in CAKE\venv

## Dependencies
None

## Installation

Clone the project.
```sh
pip3.7 install --editable .
```
in \cake directory.

## Usage

```sh
usage: cake [-h] [--cake FILENAME] [--version]

cake - automated dev environment.

optional arguments:
  -h, --help           show this help message and exit
  --cake CAKE          desired filename for project.
  --version            print "cake" version.
```
