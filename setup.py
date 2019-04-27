from setuptools import setup, find_packages

setup(
    name = 'bake',
    version = '0.1.1',
    author = 'Mar Bocatcat',
    author_email = 'mar.bocatcat@gmail.com',
    description = 'automation of my project environment',
    license = 'MIT',
    url = 'https://github.com/Marbocatcat/cake.git',
    packages = find_packages(),
    entry_points = '''
        [console_scripts]
        bake=bake.__main__:main
    '''
)
