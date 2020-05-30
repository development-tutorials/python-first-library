---
layout: page
title: About
permalink: /about/
---



This site aims to provide detailed instructions and examples for publishing Python libraries.


To correct mistakes please [Fork](https://github.com/development-tutorials/python-first-library/fork), commit changes, and then open a [Pull Request](https://github.com/development-tutorials/python-first-library/pulls). Alternatively, to report bugs and/or offer suggestions please open an [Issue](https://github.com/development-tutorials/python-first-library/issues) if none already exists for a given topic.


Example source code is available within the `master` branch of this repository...


```bash
mkdir -vp ~/git/hub/development-tutorials

cd ~/git/hub/development-tutorials

git clone git@github.com:development-tutorials/python-first-library.git
cd python-first-library
git checkout master
```


It is possible to install this example library from the `test.pypi.org` URL...


```bash
python3 -m pip install\
  --index-url https://test.pypi.org/simple/\
  --no-deps\
  python-first-library-S0AndS0
```


This is the base Jekyll theme, more info about customizing Jekyll themes, as well as basic Jekyll usage documentation are available at [jekyllrb.com](https://jekyllrb.com/)

Source code for Minima is available at GitHub: [jekyll][jekyll-organization] / [minima](https://github.com/jekyll/minima)

Source code for Jekyll is available at GitHub: [jekyll][jekyll-organization] / [jekyll](https://github.com/jekyll/jekyll)


This site's source is available within the `gh-pages` branch of this repository...


```bash
cd ~/git/hub/development-tutorials/python-first-library

git checkout gh-pages
```


Resources used to build this tutorial are listed within the ReadMe file for this project under the [Attribution](https://github.com/development-tutorials/python-first-library#attribution) section.



[jekyll-organization]: https://github.com/jekyll
