# Python First Library
[heading__top]:
  #python-first-library
  "&#x2B06; Example library for use within other Python projects"


Example library for use within other Python projects

## [![Byte size of Python First Library][badge__master__python_first_library__source_code]][python_first_library__master__source_code] [![Open Issues][badge__issues__python_first_library]][issues__python_first_library] [![Open Pull Requests][badge__pull_requests__python_first_library]][pull_requests__python_first_library] [![Latest commits][badge__commits__python_first_library__master]][commits__python_first_library__master] [![python-first-library Demos][badge__gh_pages__python_first_library]][gh_pages__python_first_library]


------


- [:arrow_up: Top of Document][heading__top]

- [:building_construction: Requirements][heading__requirements]

- [:zap: Quick Start][heading__quick_start]

  - [&#x1F9F0; Usage][heading__usage]

- [&#x1F5D2; Notes][heading__notes]

- [:card_index: Attribution][heading__attribution]

- [:balance_scale: Licensing][heading__license]


------



## Requirements
[heading__requirements]:
  #requirements
  "&#x1F3D7; Prerequisites and/or dependencies that this project needs to function properly"


Python based developer dependencies may be installed via one of the following methods...


- Scoped within current user...


```Bash
pip3 install --user setuptools twine wheel
```


- Scoped with a _Virtual Environment_ local to the directory of this project...


```Bash
pip3 install --user pipenv

pipenv install setuptools twine wheel
```


> Note, review [Python Guide -- `virtualenvs`](https://docs.python-guide.org/dev/virtualenvs/) for more information on Python Virtual Environments.


- Or scoped for the entire system...


```Bash
sudo pip3 install setuptools twine wheel
```


> Note, generally installing dependencies system-wide is not recommended.


___


## Quick Start
[heading__quick_start]:
  #quick-start
  "&#9889; Perhaps as easy as one, 2.0,..."


Clone this project...


**Linux/MacOS**


```Bash
mkdir -vp ~/git/hub/development-tutorials

cd ~/git/hub/development-tutorials

git clone git@github.com:development-tutorials/python-first-library.git
```


**Windows**


```Batch
set _organization_directory="%HOMEDRIVE%%HOMEPATH%\git\hub\development-tutorials"

if not exists %_organization_directory (
  md %_organization_directory
)

CD /D %_organization_directory

git clone git@github.com:development-tutorials/python-first-library.git
```

------


### Usage
[heading__usage]:
  #usage
  "&#x1F9F0;"


> Note the following are abbreviated instructions, check the [Tutorial][gh_pages__python_first_library] site for detailed guidance.


Example of packaging this project for publishing to Pip repository...


```Bash
python3 setup.py sdist bdist_wheel
```


Example of uploading to the testing repository...


```Bash
twine upload --repository testpypi dist/python-first-library-0.0.1*
```


Example of installing from testing repository...


```Bash
python3 -m pip install\
  --index-url https://test.pypi.org/simple/\
  --no-deps python-first-library-<YourName>
```


Example of inheriting and modifying a class from python-first-library...


```Python
#!/usr/bin/env python


from python_first_library import First_Library


class Customized_First_Library(First_Library):
    """
    Customizes First_Library class with additional initialization parameters
    """

    def __init__(self, custom_arg = None, **kwargs):
        """
        Adds `custom_arg` to initialization of parent First_Library class
        """
        super(Customized_First_Library, self).__init__(**kwargs)
        self.custom_arg = custom_arg

    def main(self, **kwargs):
        """
        Prints `custom_arg` and returns results from parent `main()` method
        """
        original_main_results = super(Customized_First_Library, self).main(**kwargs)

        print(original_main_results)
        print("self.custom_arg -> {}".format(self.custom_arg))

        return original_main_results


if __main__ == '__name__':
    """
    Code that is run if this file is executed as a script instead of imported
    """
    customized = Customized_First_Library(custom_arg = 'SPAM')
    customized.main()
```


___


## Notes
[heading__notes]:
  #notes
  "&#x1F5D2; Additional things to keep in mind when developing"


This repository may not be feature complete and/or fully functional, Pull Requests that add needed features and/or fix bugs are certainly welcomed.

___


## Attribution
[heading__attribution]:
  #attribution
  "&#x1F4C7; Resources that where helpful in building this project so far."


- [GitHub -- `github-utilities/make-readme`](https://github.com/github-utilities/make-readme)

- [Python Packaging -- Packaging Projects](https://packaging.python.org/tutorials/packaging-projects/)

- [Python Packaging -- Managing Dependencies](https://packaging.python.org/tutorials/managing-dependencies/)

- [Python Packaging -- `install_requires` vs requirements files](https://packaging.python.org/discussions/install-requires-vs-requirements/)

- [Python Packaging -- Classifiers](https://pypi.org/classifiers/)

- [Python Packaging -- Packaging -- `MANIFEST.in`](https://packaging.python.org/guides/distributing-packages-using-setuptools/#manifest-in)

- [Python Docs -- Writing the `setup.cfg` Configuration File](https://docs.python.org/3/distutils/configfile.html)

- [setuptools -- Using `find_packages()`](https://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages)

- [Medium -- How to upload your Python package to PyPi](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)

- [StackOverflow -- Publishing modules to pip and PyPi](https://stackoverflow.com/questions/56129825/)


___


## License
[heading__license]:
  #license
  "&#x2696; Legal side of Open Source"


```
Example library for use within other Python projects
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
```


For further details review full length version of [AGPL-3.0][branch__current__license] License.



[branch__current__license]:
  /LICENSE
  "&#x2696; Full length version of AGPL-3.0 License"


[badge__commits__python_first_library__master]:
  https://img.shields.io/github/last-commit/development-tutorials/python-first-library/master.svg

[commits__python_first_library__master]:
  https://github.com/development-tutorials/python-first-library/commits/master
  "&#x1F4DD; History of changes on this branch"


[python_first_library__community]:
  https://github.com/development-tutorials/python-first-library/community
  "&#x1F331; Dedicated to functioning code"

[python_first_library__gh_pages]:
  https://github.com/development-tutorials/python-first-library/tree/
  "Source code examples hosted thanks to GitHub Pages!"

[badge__gh_pages__python_first_library]:
  https://img.shields.io/website/https/development-tutorials.github.io/python-first-library/index.html.svg?down_color=darkorange&down_message=Offline&label=Demo&logo=Demo%20Site&up_color=success&up_message=Online

[gh_pages__python_first_library]:
  https://development-tutorials.github.io/python-first-library/index.html
  "&#x1F52C; Check the example collection tests"

[issues__python_first_library]:
  https://github.com/development-tutorials/python-first-library/issues
  "&#x2622; Search for and _bump_ existing issues or open new issues for project maintainer to address."

[pull_requests__python_first_library]:
  https://github.com/development-tutorials/python-first-library/pulls
  "&#x1F3D7; Pull Request friendly, though please check the Community guidelines"

[python_first_library__master__source_code]:
  https://github.com/development-tutorials/python-first-library/
  "&#x2328; Project source!"

[badge__issues__python_first_library]:
  https://img.shields.io/github/issues/development-tutorials/python-first-library.svg

[badge__pull_requests__python_first_library]:
  https://img.shields.io/github/issues-pr/development-tutorials/python-first-library.svg

[badge__master__python_first_library__source_code]:
  https://img.shields.io/github/repo-size/development-tutorials/python-first-library
