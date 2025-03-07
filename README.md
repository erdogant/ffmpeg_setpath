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

Step 1. ffmpeg_setpath downloads the ffmpeg files.

Step 2. ffmpeg_setpath stores the files in the temp-directory or the provided dirpath.

Step 3. ffmpeg_setpath adds the /bin directory to system environment.

That's it. Now you can use ffmpeg.

### Installation

```bash
pip install ffmpeg_setpath            # normal install
pip install --upgrade ffmpeg_setpath # or update if needed
```

#### Import ffmpeg_setpath package
```python
from ffmpeg_setpath import ffmpeg_setpath
ffmpeg_setpath()
```


#### References
* https://github.com/erdogant/ffmpeg_setpath

### Contribute
* All kinds of contributions are welcome!
* If you wish to buy me a <a href="https://www.buymeacoffee.com/erdogant">Coffee</a> for this work, it is very appreciated :)

### Licence
See [LICENSE](LICENSE) for details.
