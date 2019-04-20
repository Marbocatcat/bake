#!/bin/env python3
from pathlib import Path
import subprocess


class Mkenv():

    def __init__(self, name):
        self.name = name
        self.path = Path.cwd() / self.name
        self.venv_path = self.path / 'venv'
        self.file_path = self.path / self.name / f'{self.name}.py'


    def _createProject(self):
        """Factory method to create all needed files and installs virtualenv."""
        try:
            self._createDirectory()
            self._createFile()
            self._createSetup()
            self._installVenv()

        except FileExistsError as err:
            print(f'Error creating path! Error: {err}')

    def _installVenv(self):
        """Run's python's virtualenv in that target path."""

        subprocess.call(["python3", "-m", "venv", f"{self.venv_path}"])
        print(f"Creating venv in: {self.venv_path}")

    def _createFile(self):
        """Create's target file path."""
        mode = 0o772

        # creates file "/folder/folder/file.py"
        self.file_path.write_text('#/env/bin python3')
        print(f"File created: {self.file_path}")
        # chmod u+x file.py
        self.file_path.chmod(mode)
        print(f"Changed mode: {mode} for {self.name}.py")

    def _createSetup(self):
        """Create's setup files."""
        setup_path = self.path / 'setup.py'
        readme_path = self.path / 'README.md'
        git_ignore = self.path /'.gitignore'

        # create setup.py
        setup_path.write_text('#/env/bin python3')
        # create README.md
        readme_path.write_text(f'{self.name}')
        # create .gitignore
        git_ignore.write_text('/venv/\n/mkenv.egg-info\n/mkenv/__pycache__')

    def _createDirectory(self):
        """Create's needed venv directories."""
        file_path = self.path / self.name

        # creates directory folder
        Path.mkdir(file_path, parents=True)
        print(f"Path created: {self.path}")
        # creates venv "/folder/venv"
        Path.mkdir(self.venv_path)
        print(f"Venv created: {self.venv_path}")
