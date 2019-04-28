import unittest
import pathlib
import shutil

from bake import bake


class BakeTestCase(unittest.TestCase):
    def setUp(self):
        self.red_cake = bake.Bake("red_cake")

    def test_args_name(self):
        """Tests self.name"""
        self.assertEqual(self.red_cake.name, "red_cake")

        self.red_cake.name = "velvel_cake"
        self.assertEqual(self.red_cake.name, "velvel_cake")

    def test_args_path(self):
        """Tests self.path"""
        test_against = pathlib.Path.cwd() / self.red_cake.name
        self.assertEqual(self.red_cake.path, test_against)

    def test_args_venv(self):
        """Tests self.venv_path"""
        test_against = pathlib.Path.cwd() / self.red_cake.name / "venv"
        self.assertEqual(self.red_cake.venv_path, test_against)

    def test_file_path(self):
        """Tests self.file_path"""
        test_against = pathlib.Path.cwd() / self.red_cake.name / self.red_cake.name / "red_cake.py"
        self.assertEqual(self.red_cake.file_path, test_against)

    def test_create_directory(self):
        """Test _create_directory_ function"""

        # Tests return value
        self.assertTrue(self.red_cake._create_directory(), 1)

        # Tests error raised
        with self.assertRaises(FileExistsError):
            self.red_cake._create_directory()

    def tearDown(self):
        red_cake_path = pathlib.Path.cwd() / 'red_cake'
        if red_cake_path.exists():
            shutil.rmtree(red_cake_path)
            print('tear down complete')


if __name__ == "__main__":
    unittest.main()
