# gearpy

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)

**gearpy** is a Python module that auto-optimizes CPU-bound code using parallel threads, bypassing the GIL, with a simple decorator.

## Features
- Easy-to-use `@optimize` decorator
- Auto-runs functions in true threads
- Boosts CPU-heavy code performance

## Install
_(Not on PyPI yet—coming soon)_

## Usage
```python
from gearpy import optimize

@optimize
def heavy_func(x):
    for _ in range(10**6):
        x = x ** 0.5 + x ** 1.5
    return x
