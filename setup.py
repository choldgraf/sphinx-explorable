import os
from pathlib import Path
from setuptools import setup, find_packages

version = [
    line
    for line in Path("sphinx_ink/__init__.py").read_text().split("\n")
    if "__version__" in line
]
version = version[0].split(" = ")[-1].strip('"')

with open("./README.rst", "r") as ff:
    readme_text = ff.read()

setup(
    name="sphinx-ink",
    version=version,
    description="Add a toggle button to items on a page.",
    long_description=readme_text,
    long_description_content_type="text/x-rst",
    author="Chris Holdgraf",
    author_email="choldgraf@berkeley.edu",
    url="https://github.com/choldgraf/sphinx-ink",
    license="MIT License",
    packages=find_packages(),
    package_data={
        "sphinx_ink": ["_static/togglebutton.css_t", "_static/togglebutton.js"]
    },
    install_requires=["setuptools", "wheel", "sphinx", "docutils"],
    extras_require={"sphinx": ["myst_nb"]},
    classifiers=["License :: OSI Approved :: MIT License"],
)
