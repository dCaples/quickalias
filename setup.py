import codecs
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()

VERSION = "3.1.2"
DESCRIPTION = "Creates permanent aliases"
# LONG_DESCRIPTION = "Creates permanent aliases so you don't have to open your shell config file"


setup(
    name="quickalias",
    version=VERSION,
    author="Decator (Aidan Neal) & dCaples",
    author_email="decator.c@proton.me",
    url="https://github.com/dCaples/quickalias",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    install_requires=[],
    py_modules=['quickalias'],
    license='GPLv3',
    entry_points = {'console_scripts': ['quickalias = quickalias:main']},
    keywords=["python", "alias", "shell",
              "config", "scriptable", "commandline"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",

    ]
)
