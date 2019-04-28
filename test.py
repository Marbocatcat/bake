import unittest
import pathlib

from bake import bake


class BakeTestCase(unittest.TestCase):

    def test_args_name(self):
        """Tests self.name"""
        red_cake = bake.Bake("red_cake")
        self.assertEqual(red_cake.name, "red_cake")

        red_cake.name = "velvel_cake"
        self.assertEqual(red_cake.name, "velvel_cake")

    def test_args_path(self):
        """Tests self.path"""
        red_cake = bake.Bake("red_cake")
        test_against = pathlib.Path.cwd() / red_cake.name
        self.assertEqual(red_cake.path, test_against)

    def test_args_venv(self):
        """Tests self.venv_path"""
        red_cake = bake.Bake("red_cake")
        test_against = pathlib.Path.cwd() / red_cake.name / "venv"
        self.assertEqual(red_cake.venv_path, test_against)

    def test_file_path(self):
        """Tests self.file_path"""
        vanilla_cake = bake.Bake("vanilla_cake")
        test_against = pathlib.Path.cwd() / vanilla_cake.name / vanilla_cake.name / "vanilla_cake.py"
        self.assertEqual(vanilla_cake.file_path, test_against)


if __name__ == "__main__":
    unittest.main()
