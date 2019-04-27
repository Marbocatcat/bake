import unittest

from bake import bake


class BakeTestCase(unittest.TestCase):
    def test_bake_cake(self):
        cake = bake.Bake('test_cake')

        with self.assertRaises(FileExistsError):
            cake._create_cake()

    def test_bake_num(self):

        with self.assertRaises(TypeError):
            bake.Bake(1)


if __name__ == "__main__":
    unittest.main()

