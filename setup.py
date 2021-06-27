import os
import codecs
import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


# This call to setup() does all the work
setup(
    name="flaskbp",
    version=get_version("flaskbp/__init__.py"),
    description=(
        "A python package for basic Flask app boilerplate."
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/frankhart2018/flaskbp",
    author="Siddhartha Dhar Choudhury",
    author_email="sdharchou@gmail.com",
    license="GNU General Public License v3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
    ],
    packages=[package for package in find_packages()],
    package_data={
        "flaskbp": [
            "files/app.py",
            "files/index.html",
            "files/jquery.min.js",
            "files/main.js",
            "files/utils.js",
            "files/styles.css",
            "files/sweetalert.min.js",
        ]
    },
    entry_points={
        'console_scripts': [
            'flaskbp = flaskbp.generate:gen_bp'
        ]
    },
)