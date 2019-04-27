from setuptools import setup, find_packages

setup(
    name = 'mkenv',
    version = '0.1.1',
    author = 'Mar Bocatcat',
    author_email = 'mar.bocatcat@gmail.com',
    description = 'automation of my project environment',
    license = 'MIT',
    url = 'https://github.com/Marbocatcat/mkenv.git',
    packages = find_packages(),
    entry_points = '''
        [console_scripts]
        mkenv=mkenv.__main__:main
    '''
)
