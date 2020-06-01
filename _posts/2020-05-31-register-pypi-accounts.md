---
layout: post
title:  "Register PyPi Accounts"
date:   2020-05-31 16:11:56 -0700
categories: python library tutorial
excerpt: ''
---



## Testing Repository
[heading__testing_repository]: #testing-repository "Python testing repository links"


- [`test.pypi.org` -- Register](https://test.pypi.org/account/register/)

- [`test.pypi.org` -- API Token](https://test.pypi.org/manage/account/#api-tokens)

- [`test.pypi.org` -- 2FA](https://pypi.org/manage/account/totp-provision)


Utilizing the testing repository is a good idea, because deleting and/or editing mistakes within the official publishing repository is not generally allowed.


Testing Repository installation syntax adds `--index-url https://test.pypi.org/simple/` and _`--no-deps <Package_Name>-<Account_Name>`_ options, eg...


```Bash
python3 -m pip install\
  --index-url https://test.pypi.org/simple/\
  --no-deps python-first-library-S0AndS0
```


> Note, the `--no-deps` flag tells Pip to **not** install dependencies from the testing URL, this is important to avoid errors during installation, and testing.


------


## Publish Repository
[heading__publish_repository]: #publish-repository "Python publishing repository links"


- [`pypi.org` -- Register](https://pypi.org/account/register/)

- [`pypi.org` -- API Token](https://pypi.org/manage/account/#api-tokens)

- [`pypi.org` -- 2FA](https://pypi.org/manage/account/totp-provision)


Please do **not** skip setting up 2 Factor Authentication, because you'll be publishing code for others to make use of.


------


## Example `~/.pypirc`
[heading__example_pypirc]: #example-~pypirc "Example pypirc configuraiton file"


```
[pypi]
  username = __token__
  ## Test
  password = pypi-API_TEST_KEY...
  ## Publish
  # password = pypi-API_PUBLISH_KEY...
```
