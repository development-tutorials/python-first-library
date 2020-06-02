---
layout: home
list_title: Steps
---



**Warning** this tutorial is a draft, and until this warning is removed pages/posts may move! In other-words. please avoid bookmarking individual posts until this warning is removed. To correct any inaccuracies [Pull Requests](https://github.com/development-tutorials/python-first-library) are very welcomed.


___


This tutorial is intended for those that wish to publish a library or libraries to Python Pip repository. Before following this guide, readers should have Python installed, as well as some knowledge of reading and writing Python code. The official [getting started](https://www.python.org/about/gettingstarted/) documentation from Python, is an excellent resource if statring out or if refreshing one's knowledge feels needed.


Python Language source may be downloaded from [`python.org`](https://www.python.org/downloads/) for most Operating Systems, alternatively most Linux distributions have python available via package manager...


```Bash
## Arch inspired distributions
sudo packman -S python3 python3-pip

## Debian derived distributions
sudo apt-get install python3 python3-pip
```


Most, if not all, of the command-line examples will be for a Bash (Born Again SHell) environment, eg...


- _`cd ~/somewhere`_ -- _`c`hange `d`irectory_ to _`somewhere`_ under the current user's home (_`~`_) directory

- _`mkdir ~/somewhere/another-thing`_ -- _`m`a`k`e `dir`ectory_ under the current user's home (_`~`_) directory with the path of _`somewhere/another-thing`_

- _`touch ~/somewhere/another-thing/file.ext`_ -- update last modified time, or create an empty file, named _`file.ext`_ under the current user's home (_`~`_) directory with a directory path of _`somewhere/another-thing`_

- Long command-line examples are split using a backslash (`\`) to escape new-lines, and lines that follow are indented by two spaces (`  `)...


```Bash
executable-name --param-one "first modifier"\
  --param-two "second modifier"\
  --flag-one\
  --flag-two
```


As much as possible, commands specific to Bash will be limited to above examples. Commands for Git and Python code examples _should_ otherwise be environment agnostic so long as your device has applications and dependencies installed.
