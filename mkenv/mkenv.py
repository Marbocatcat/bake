#!/bin/env python3
from pathlib import Path
import subprocess


class Mkenv():

    def __init__(self, name):
        self.name = name
        self.path = Path.cwd() / self.name

    def createProject(self):

        try:
            self.createDirectory()
            self.createFile()
            self.createSetup()
            self.installVenv()
            return True

        except FileExistsError as err:
            print(f'Error creating path! Error: {err}')
            return False

    def installVenv(self):
        venv_path = self.path / 'venv'

        subprocess.call(["python3", "-m", "venv", f"{venv_path}"])
        print(f"Creating venv in: {venv_path}")

    def createFile(self):
        file_path = self.path / self.name / f'{self.name}.py'

        # creates file "/folder/folder/file.py"
        file_path.write_text('#/env/bin python3')
        print(f"File created: {file_path}")
        # chmod u+x file.py
        file_path.chmod(227)
        print(f"Changed mode: 774 for {self.name}.py")

    def createSetup(self):
        setup_path = self.path / 'setup.py'
        readme_path = self.path / 'README.md'

        # create setup.py
        setup_path.write_text('#/env/bin python3')
        # create README.md
        readme_path.write_text(f'{self.name}')

    def createDirectory(self):
        venv_path = self.path / 'venv'
        file_path = self.path / self.name

        # creates directory folder
        Path.mkdir(file_path, parents=True)
        print(f"Path created: {self.path}")
        # creates venv "/folder/venv"
        Path.mkdir(venv_path)
        print(f"Venv created: {venv_path}")

    def activate(self):
        #TODO: DOES NOT WORK!
        activate_venv = subprocess.Popen([f'source {self.name}/venv/bin/activate'], shell=True)
        print(activate_venv.communicate())
