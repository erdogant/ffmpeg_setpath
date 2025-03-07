# ffmpeg_setpath

[![Python](https://img.shields.io/pypi/pyversions/ffmpeg_setpath)](https://img.shields.io/pypi/pyversions/ffmpeg_setpath)
[![Pypi](https://img.shields.io/pypi/v/ffmpeg_setpath)](https://pypi.org/project/ffmpeg_setpath/)
[![Docs](https://img.shields.io/badge/Sphinx-Docs-Green)](https://erdogant.github.io/ffmpeg_setpath/)
[![LOC](https://sloc.xyz/github/erdogant/ffmpeg_setpath/?category=code)](https://github.com/erdogant/ffmpeg_setpath/)
[![Downloads](https://static.pepy.tech/personalized-badge/ffmpeg_setpath?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month)](https://pepy.tech/project/ffmpeg_setpath)
[![Downloads](https://static.pepy.tech/personalized-badge/ffmpeg_setpath?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/ffmpeg_setpath)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/ffmpeg_setpath/blob/master/LICENSE)
[![Forks](https://img.shields.io/github/forks/erdogant/ffmpeg_setpath.svg)](https://github.com/erdogant/ffmpeg_setpath/network)
[![Issues](https://img.shields.io/github/issues/erdogant/ffmpeg_setpath.svg)](https://github.com/erdogant/ffmpeg_setpath/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
![GitHub Repo stars](https://img.shields.io/github/stars/erdogant/ffmpeg_setpath)
![GitHub repo size](https://img.shields.io/github/repo-size/erdogant/ffmpeg_setpath)
[![Donate](https://img.shields.io/badge/Support%20this%20project-grey.svg?logo=github%20sponsors)](https://erdogant.github.io/ffmpeg_setpath/pages/html/Documentation.html#)
<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->


* ``ffmpeg_setpath`` is Python package

# 
**Star this repo if you like it! ⭐️**
#

ffmpeg_setpath is to set the path for ffmpeg for Windows environments.
It will download ffmpeg and include the paths into the system environment.
There are multiple steps that are taken to set the ffmpeg path in the system environment.


The following steps are automated:

  * Step 1. Download the ffmpeg file.
  * Step 2. Store the files in the temp-directory or the provided dirpath.
  * Step 3. Add the /bin directory to system environment.

### Installation

```bash
pip install ffmpeg_setpath            # normal install
pip install --upgrade ffmpeg_setpath # or update if needed
```

#### Set ffmpeg to your system environment:
```python
from ffmpeg_setpath import ffmpeg_setpath
ffmpeg_setpath()
```

#### Specify your ffmpeg directory:
```python
from ffmpeg_setpath import ffmpeg_setpath
ffmpeg_setpath(dirpath=r'c:/ffmpeg/')
```

#### Start all over and force download all files, unzip, and set to system environment:
```python
from ffmpeg_setpath import ffmpeg_setpath
ffmpeg_setpath(force=True)
```

#### Set specified path in environment
```python
import ffmpeg_setpath as ff
f.set_path(dirpath=r'c:/temp/ffmpeg/')
```

#### Check whether path or string exists in system
```python
import ffmpeg_setpath as ff

# Check for path
out_bool = ff.check(r'c:/ffmpeg/bin', exact_match=True)

# Check for string
out_list = ff.check(r'ffmpeg', exact_match=False)
```

#### Force to set path in env
```python
import ffmpeg_setpath as ff

ff.set_path(r'c:/temp/ffmpeg/')
```

#### Remove specified path from environment
```python
import ffmpeg_setpath as ff

ff.remove(r'c:\ffmpeg1\bin')
```

#### Show all paths in environment
```python
import ffmpeg_setpath as ff

ff.printe()
```


#### References
* https://github.com/erdogant/ffmpeg_setpath

### Contribute
* All kinds of contributions are welcome!
* If you wish to buy me a <a href="https://www.buymeacoffee.com/erdogant">Coffee</a> for this work, it is very appreciated :)

### Licence
See [LICENSE](LICENSE) for details.
