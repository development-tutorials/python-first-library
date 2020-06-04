---
layout: post
title:  "Package Setup"
date:   2020-06-04 16:11:56 -0700
categories: python library tutorial
excerpt: 'Example `setup.py` script and related configuration files'
---



Change current working directory to your project repository...


```bash
cd ~/git/hub/development-tutorials/python-first-library
```


------


## [#][heading__manifest_in] `MANIFEST.in`
[heading__manifest_in]: #-manifestin "Defines paths that should be explicitly included or excluded"


The `MANIFEST.in` configuration file is where project files that are not automatically detected can either be included, or excluded, within build process...


```
include .github/README.md
```


... for this tutorial the ReadMe file is included, because by default `setuptools` will not include files within the `.github` directory.


------


## [#][heading__setup_cfg] `setup.cfg`
[heading__setup_cfg]: #-setupcfg "Defines metadata and other project properties"


The `setup.cfg` configuration file is able to define much more than `metadata`, and the official [Python Docs -- Writing the `setup.cfg` Configuration File](https://docs.python.org/3/distutils/configfile.html) is worthy of review...


```cfg
[metadata]
description-file = .github/README.md
```


... for this tutorial the the ReadMe file is defined as the `description-file` to notify web-based documentation scripts where to pull data from.


------


## [#][heading__setup_py] `setup.py`
[heading__setup_py]: #-setuppy "Script that `pip install package-name` command calls"


The `setup.py` script is called by `setuptools`


```Python
#!/usr/bin/env python3


from setuptools import (find_packages, setup)


with open(".github/README.md", "r") as fh:
    long_description = fh.read()


setup(
    name = 'watch_path',
    version = '0.0.1',
    author = '<account_name>',
    author_email = '<account_name>@<domain>.<tld>',
    description = 'An example Python library',
    license = 'AGPL-3.0'
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/development-tutorials/python-first-library',
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'watch_path = python_first_library.cli:main'
        ],
    },
    install_requires = [],
    classifiers = [
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX :: Linux',
    ],
)
```


### [#][heading__notes_about_setup_py] Notes about `setup.py`
[heading__notes_about_setup_py]: #-notes-about-setuppy "Quick descriptions list of parameters for `setup` method"


- `name`, the name of your project this value is pre-pended within project archive files under the `dist/` directory
- `version`, tag and/or release version this value is inserted within project archive files under the `dist/` directory
- `author`, your account name
- `author_email`, a valid email address used to contact you
- `description`, short (less than 80 characters) description of your project
- `license`, the code/abbreviation for chosen license, the [OpenSource.org chart](https://opensource.org/licenses/category) lists most of the popular licenses with their abbreviations
- `url` HTTP URL to source code for your project
- `entry_points["console_scripts"]` list name of executable(s), import path, and function to call
- `classifiers`, check the [Python Packaging -- Classifiers](https://pypi.org/classifiers/) for complete listing of all valid options
