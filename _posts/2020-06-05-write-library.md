---
layout: post
title:  "Write Library"
date:   2020-06-05 16:11:56 -0700
categories: python library tutorial
excerpt: 'Example `First_Library` class'
---



Change current working directory to your project repository...


```bash
cd ~/git/hub/development-tutorials/python-first-library
```


------


## `python_first_library/__init__.py`
[python_first_library/__init__.py]: #python_first_library__init__py ""


```Python
#!/usr/bin/env python3


if __name__ == '__main__':
    raise NotImplementedError('Please import First_Library instead')


__license__ = """
First Python Library example usage script
Copyright (C) 2020 S0AndS0

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


class First_Library(object):
    """docstring for First_Library."""

    def __init__(self, **keyword_arguments):
        super(First_Library, self).__init__()
        self.keyword_arguments = keyword_arguments

    def print_keyword_arguments(self):
        print(self.keyword_arguments)
```


When installed via pip, the class from this library will be importable via `from python_first_library import First_Library`
