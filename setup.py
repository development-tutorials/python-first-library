#!/usr/bin/env python3


from setuptools import (find_packages, setup)


with open(".github/README.md", "r") as fh:
    long_description = fh.read()


setup(
    name = 'python_first_library',
    version = '0.0.1',
    author = 'S0AndS0',
    author_email = 'StrangerThanBland@gmail.com',
    description = 'An example Python library',
    license = 'AGPL-3.0',
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
