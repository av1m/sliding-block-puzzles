# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license_ = f.read()

setup(
    name="sliding_puzzle",
    version="0.0.1dev",
    description="Sliding block/tile puzzle solver using multiple algorithms",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="PARDINI Raphael, MIMOUN Avi",
    author_email="4v1m+github@protonmail.ch",
    url="https://github.com/av1m/sliding-block-puzzles",
    project_urls={
        "Bug Tracker": "https://github.com/av1m/sliding-block-puzzles/issues",
        "Project Management": "https://github.com/av1m/sliding-block-puzzles/projects",
    },
    license=license_,
    packages=find_packages(),
    entry_points={"console_scripts": ["sliding_puzzle=sliding_puzzle.__main__:main"]},
    python_requires=">=3.9",
)
