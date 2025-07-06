#!/usr/bin/env python3
"""
Setup script for Snake Game
A classic terminal-based snake game implementation in Python.
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read the requirements file
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="snake-game",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A classic Snake game implementation in Python using curses",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/snake-game",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/snake-game/issues",
        "Source": "https://github.com/yourusername/snake-game",
        "Documentation": "https://github.com/yourusername/snake-game#readme",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment :: Arcade",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="snake, game, terminal, curses, arcade, python",
    packages=find_packages(),
    py_modules=["snake_game"],
    python_requires=">=3.6",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "snake-game=snake_game:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    platforms=["any"],
    license="MIT",
    python_requires=">=3.6",
) 