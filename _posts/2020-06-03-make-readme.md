---
layout: post
title:  "Make ReadMe"
date:   2020-06-03 16:11:56 -0700
categories: python library tutorial
excerpt: "A project's ReadMe file is often the first documents users will review"
---



Change current working directory to your project repository...


```bash
cd ~/git/hub/development-tutorials/python-first-library
```


## Option One
[Option One]: #option-two "Make a simple ReadMe file"


Make a simple ReadMe file...


```bash
cd ~/git/hub/development-tutorials/python-first-library


mkdir .github
touch .github/README.md
```


Following is an example template that can be edited manually...


{% raw %}
```markdown
# Python First Library
[heading__top_of_document]: #python-first-library "Top of document"


------


- [Python First Library][heading__top_of_document]

- [Installation][heading__installation]

- [Usage][heading__usage]

- [Notes][heading__notes]

- [Attribution][heading__attribution]

- [License][heading__license]


------


## Installation
[heading__installation]: #installation "How to install this project"


Install to user account via...


    pip3 install --user python_first_library


## Usage
[heading__usage]: #usage "How to utilize this project"


Import within Python shell or script via...


    from python_first_library import First_Library


## Notes
[heading__notes]: #notes "Things to keep in mind when using the project"


    Anything else note worthy?


## Attribution
[heading__attribution]: #attribution "Resources that where helpful in building this project"


- [GitHub -- `development-tutorials/python-first-library`](https://github.com/development-tutorials/python-first-library)


## License
[heading__license]: #license "Legal side of Open Source software"


This project is released under the [AGPL version 3](/LICENSE) license


```
{% endraw %}


------


## Option Two
[Option Two]: #option-two "Initialize ReadMe file via template"


The following examples make use of [GitHub -- `github-utilities/make-readme`](https://github.com/github-utilities/make-readme) project which builds ReadMe files from MustacheJS templates.


Initialize ReadMe file via template...


```bash
mkdir -vp ~/git/hub/github-utilities

cd ~/git/hub/github-utilities

git clone git@github.com:github-utilities/make-readme.git

cd ~/git/hub/github-utilities/make-readme
```


Install NPM dependencies...


```bash
npm install
```


**Edit `github-utilities/make-readme` -- `dataView.json`**


```json
{
  "gfm": true,
  "email": "account@host.tld",
  "author": "S0AndS0",
  "organization": "development-tutorials",
  "repository": "python-first-library",
  "output_directory": "~/git/hub/development-tutorials/python-first-library",
  "description": "Example library for use within other Python projects",
  "include_notes": true,
  "include_shields_io": true,
  "license": "AGPL-3.0",
  "gh_pages": true,
  "verbose": true,
  "clobber": true,
  "quick_start": {
    "is_awk_script": false,
    "is_github_action": false,
    "is_node_package": false,
    "is_python_package": true,
    "is_submodule": false
  },
  "requirements": {
    "utilizes_awk": false,
    "utilizes_npm": false,
    "utilizes_github_actions": false,
    "utilizes_pip": false,
    "utilizes_submodules": false
  },
  "files": [
    {
      "in_path": ".mustache/.github/README.md.mst",
      "out_path": ".github/README.md",
      "partials": [
        ".mustache/partials/readme/quick_start/clone.md.mst",
        ".mustache/partials/readme/quick_start/is_awk_script.md.mst",
        ".mustache/partials/readme/quick_start/is_node_package.md.mst",
        ".mustache/partials/readme/quick_start/is_github_action.md.mst",
        ".mustache/partials/readme/quick_start/is_python_package.md.mst",
        ".mustache/partials/readme/quick_start/is_submodule.md.mst",
        ".mustache/partials/readme/requirements/utilizes_awk.md.mst",
        ".mustache/partials/readme/requirements/utilizes_github_actions.md.mst",
        ".mustache/partials/readme/requirements/utilizes_npm.md.mst",
        ".mustache/partials/readme/requirements/utilizes_pip.md.mst",
        ".mustache/partials/readme/requirements/utilizes_submodules.md.mst",
        ".mustache/partials/readme/notes.md.mst"
      ]
    }
  ]
}
```


Make output directory for ReadMe file and generate new ReadMe file from template...


```bash
mkdir ~/git/hub/development-tutorials/python-first-library/.github

npm run make-readme
```
