---
layout: post
title:  "Setup Environment"
date:   2020-06-01 16:11:56 -0700
categories: python library tutorial
excerpt: 'List of dependencies installed via Pip and links to relevant documentation'
---



Install `pip` by following [PyPa documentation](https://pip.pypa.io/en/stable/installing/) if `pip3 --version` returns an error.


Install Python environment dependencies to user account...


```bash
pip3 install --user setuptools twine wheel
```


Documentation links for above dependencies;


- [Read The Docs -- `setuptools`](https://setuptools.readthedocs.io/en/latest/) _"Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects..."_

- [Read The Docs -- `twine`](https://twine.readthedocs.io) _"Twine is a utility for publishing Python packages on PyPI."_

- [Read The Docs -- `wheel`](https://wheel.readthedocs.io) _"This library is the reference implementation of the Python wheel packaging standard, as defined in PEP 427."_
