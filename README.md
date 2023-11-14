# backports.httpmethod

[![PyPI - Version](https://img.shields.io/pypi/v/backports.httpmethod.svg)](https://pypi.org/project/backports.httpmethod)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/backports-httpmethod.svg)](https://pypi.org/project/backports.httpmethod)

A backport of Python 3.11+ [`http.HTTPMethod`](https://docs.python.org/3/library/http.html#http.HTTPMethod) enum for Python 3.7+.

-----

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install backports.httpmethod
```

## Usage

```python
import sys

if sys.version_info >= (3, 11):
    from http import HTTPMethod
else:
    from backports.httpmethod import HTTPMethod


HTTPMethod.GET == 'GET'  # True
HTTPMethod.GET.value  # 'GET'
HTTPMethod.GET.description  # 'Retrieve the target.'
list(HTTPMethod)[:3] # [<HTTPMethod.GET: 'GET'>, <HTTPMethod.HEAD: 'HEAD'>, <HTTPMethod.POST: 'POST'>]
```

## License

`backports-httpmethod` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
