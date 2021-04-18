# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="sliding_puzzle",
    version="0.0.1dev",
    description="Sliding block/tile puzzle solver using multiple algorithmsms",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="PARDINI Raphael, MIMOUN Avi",
    author_email="4v1m+github@protonmail.ch",
    url="https://github.com/av1m/sliding-block-puzzles",
    project_urls={
        "Bug Tracker": "https://github.com/av1m/sliding-block-puzzles/issues",
        "Project Management": "https://github.com/av1m/sliding-block-puzzles/projects",
    },
    license=license,
    packages=find_packages(),
    python_requires=">=3.8",
)
