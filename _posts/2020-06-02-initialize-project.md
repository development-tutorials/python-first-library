---
layout: post
title:  "Initialize Project"
date:   2020-06-02 16:11:56 -0700
categories: python library tutorial
excerpt: 'Instructions for setting up file and directory structure for new library'
---



Make directory path(s) to keep things organized...


```bash
mkdir -vp ~/git/hub/development-tutorials
```


Initialize new Git repository...


```bash
git init ~/git/hub/development-tutorials/python-first-library
```


> Note, throughout this tutorial the `python-first-library` repository directory should be replaced with the directory name for your library.


Change current working directory to your new project repository...


```bash
cd ~/git/hub/development-tutorials/python-first-library
```


... add `hub` as a remote...


```bash
git remote add hub git@github.com:development-tutorials/python-first-library.git
```


> Note, URL syntax is _`git@github.com:<account>/<repository>.git`_


... touch files for `setuptools` into existence...


```bash
touch .gitignore
touch MANIFEST.in
touch requirements.txt
touch setup.cfg
touch setup.py
```


... finally make directory structure for project source code, and touch files for library and Command Line Interface example into existence...


```bash
mkdir -vp python_first_library/cli


touch python_first_library/__init__.py
touch python_first_library/cli/__init__.py
```


## Notes about files
[heading__notes_about_files]: #notes-about-files ""


- `.gitignore` defines directory and file patterns that Git should ignore from version tracking

- `MANIFEST.in` defines files not automatically detected by `setuptools` that need to be included within package archive

- `requirements.txt` should define developer dependencies, note install dependencies will need to be defined within `setup.py` file

- `setup.cfg` defines metadata about this project and may be used by code linters (code style enforcement tools)

- `setup.py` is read/executed during installation process when _`pip install <name>`_ is issued by users of this project

- `python_first_library/__init__.py` will contain the main class(s) for this project that other projects should `import`

- `python_first_library/cli/__init__.py` will contain fully functional example usage of project code as a command line application
