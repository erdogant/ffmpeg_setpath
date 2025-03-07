from ffmpeg_setpath.ffmpeg_setpath import (
    ffmpeg_setpath,
    set_path,
    remove,
    printe,
    wget,
    )


__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '1.0.0'

# module level doc-string
__doc__ = """
ffmpeg_setpath
=====================================================================

ffmpeg_setpath is to set the path for ffmpeg in the system envoirement.
Based on the operating system, ffmpeg will be downloaded and added to the system environment.
The following steps are all automated.

Step 1. Download ffmpeg.
Step 2. Store ffmpeg files on disk in temp-directory or the provided dirpath.
Step 3. Add the /bin directory to environment.

Example
-------
>>> from ffmpeg_setpath import ffmpeg_setpath
>>> ffmpeg_setpath()

References
----------
https://github.com/erdogant/ffmpeg_setpath

"""
