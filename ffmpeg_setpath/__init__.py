from ffmpeg_setpath.ffmpeg_setpath import (
    ffmpeg_setpath,
    wget,
    )


__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '1.0.0'

# module level doc-string
__doc__ = """
ffmpeg_setpath
=====================================================================

ffmpeg_setpath is to set the path for graphviz for windows machines.
Based on the operating system, it will download graphviz and include the paths into the system environment.
There are multiple steps that are taken to set the Graphviz path in the system environment.
The first two steps are automatically skipped if already present.

Step 1. Downlaod Graphviz.
Step 2. Store Graphviz files on disk in temp-directory or the provided dirpath.
Step 3. Add the /bin directory to environment.

Example
-------
>>> from ffmpeg_setpath import ffmpeg_setpath
>>> ffmpeg_setpath()

References
----------
https://github.com/erdogant/ffmpeg_setpath

"""
