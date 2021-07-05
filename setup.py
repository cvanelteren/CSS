from setuptools import setup
from setuptools.extension import Extension, find_packages

authors = ["Casper van Elteren"]

# compiled code
exts = []
packages = find_packages(include = "./src")
setup(
        name = name,
        author = authors,
        ext_modules = exts,
        packages = packages,
        )
