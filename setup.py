from setuptools import setup

setup(
    name='aoc',
    version='1.0',
    description='advent of code',
    author='robin cosbey',
    packages=['aoc'],
    install_requires=['pandas==2.1.3', 'advent-of-code-data', 'beautifulsoup4==4.12.2']
)
