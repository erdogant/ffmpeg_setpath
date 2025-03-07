"""Set ffmpeg system path.
# Name        : ffmpeg_setpath.py
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# github      : https://github.com/erdogant/ffmpeg_setpath
# Licence     : See licences
"""

import os
import sys
import requests
import logging
import zipfile
import tempfile
import re
import shutil

NAME_WIDTH = max(len(__name__), 12)
logger = logging.getLogger('')
[logger.removeHandler(handler) for handler in logger.handlers[:]]
logging.basicConfig(format=f"%(asctime)s [%(name)-{NAME_WIDTH}s]> %(levelname)-8s> %(message)s", datefmt="%d-%m-%y %H:%M:%S", level=logging.INFO)
logger = logging.getLogger(__name__)


# %% Get ffmpeg path and include into local PATH
def ffmpeg_setpath(dirpath=None, force : bool = False, version : str = 'latest', verbose: [str, int] = 'info'):
    """Set the ffmpeg path.

    All the steps are automated that needs to be done to set the ffmpeg path in the system environment for windows/unix machines.
    ffmpeg files are downloaded from https://www.gyan.dev/ffmpeg/builds/ but the .7z file gives troubles in various systems, and
    therefore a zip file is created instead and put on the Github source (Full ffmpeg version: 2025-03-06).

    Steps that are automated:
    1. Download ffmpeg.
    2. Store ffmpeg files on disk in temp-directory or the provided dirpath.
    3. Add the /bin directory to environment.

    Parameters
    ----------
    dirpath : String, optional
        Pathname of directory to save ffmpeg files.
        None: System temp directory
    version : string (default: 'latest')
        'latest': Download the latest ffmpeg from github source. (note that this is likely not the latest that is available at ffmpeg).
    force : bool (default: False)
        True: Remove all files and start all over again.
        False: Return if ffmpeg is found in system env.
    verbose : [str, int], optional
        Set the verbose messages using string or integer values.

    Returns
    -------
    None.

    """
    # Set the logger
    set_logger(verbose=verbose)

    # Extract path from URL
    dirpath = get_setpath(dirpath)

    # Remove the ffmpeg directory and all its contents.
    if force:
        # Remove dir from disk
        shutil.rmtree(dirpath)
        # Now again create the directory because it is removed
        dirpath = get_setpath(dirpath)

    # Set path based on OS
    if get_platform() == "windows":
        # Set windows path
        finPath = set_ffmpeg_windows(dirpath, version=version, force=force)
    else:
        # Set unix path
        finPath = set_ffmpeg_unix(dirpath)

    return finPath


# %%
def set_ffmpeg_unix(dirpath, version='latest', force=False):
    """Set ffmpeg path on Unix-based systems.

    https://github.com/BtbN/FFmpeg-Builds/releases

    Parameters
    ----------
    dirpath : str
        Path where ffmpeg should be installed.
    version : str, optional
        Version of ffmpeg to download, by default 'latest'.
    force : bool, optional
        If True, force reinstallation, by default False.

    Returns
    -------
    str
        Final path where ffmpeg is installed.
    """
    if version == 'latest':
        URL = 'https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl-shared.tar.xz'
    else:
        logger.info('Other versions are not available at this point. <downloading latest from source>')

    # Final path where ffmpeg binary is expected
    finPath = os.path.abspath(os.path.join(dirpath, 'ffmpeg'))

    # Check if already installed
    if os.path.exists(finPath) and not force:
        logger.info('ffmpeg is already installed and set in system environment.')
    else:
        # Download ffmpeg to disk
        archive_path = os.path.join(dirpath, 'ffmpeg.tar.xz')
        logger.info(f'Downloading ffmpeg from {URL}...')
        wget.download(URL, archive_path)

        # Extract ffmpeg
        logger.info('Extracting ffmpeg...')
        shutil.unpack_archive(archive_path, dirpath)
        os.remove(archive_path)  # Clean up archive

        # Locate the extracted directory
        extracted_dirs = [d for d in os.listdir(dirpath) if os.path.isdir(os.path.join(dirpath, d))]
        if extracted_dirs:
            extracted_dir = os.path.join(dirpath, extracted_dirs[0])
            bin_path = os.path.join(extracted_dir, 'ffmpeg')
            shutil.move(bin_path, finPath)  # Move binary to the target location
            shutil.rmtree(extracted_dir)  # Clean up extracted folder

        # Add to system path
        set_path(dirpath)

    return finPath


# %%
def set_ffmpeg_windows(dirpath, version='latest', force=False):
    if version == 'latest':
        URL = ['https://erdogant.github.io//packages/ffmpeg/ffmpeg-2025-03-06-git-696ea1c223-full_build.zip',
               'https://erdogant.github.io//packages/ffmpeg/ffmpeg-2025-03-06-git-696ea1c223-full_build_1.zip',
               'https://erdogant.github.io//packages/ffmpeg/ffmpeg-2025-03-06-git-696ea1c223-full_build_2.zip',
               'https://erdogant.github.io//packages/ffmpeg/ffmpeg-2025-03-06-git-696ea1c223-full_build_3.zip']
    else:
        logger.info('Other versions are not available at this point. <downloading latest from github source>')

    # Point directly to the bin
    finPath = os.path.abspath(os.path.join(dirpath, 'bin'))

    # Check whether already in env.
    if finPath in os.environ["PATH"] and (not force):
        logger.info('ffmpeg is already set in system environment.')
    else:
        # Download from URL
        for url in URL:
            # Download from url
            gfile = download_package(url, dirpath, force_download=force)
            # Extract file to disk
            _ = extract_files(dirpath, gfile)

        # Add to system env
        set_path(finPath)

    return finPath


# %%
def set_path(dirpath, force: bool=False, verbose: [str, int] = 'info'):
    """Set directory to system path.

    Parameters
    ----------
    dirpath : String, optional
        Pathname of directory to save ffmpeg files.
        None: System temp directory
    force : bool (default: False)
        True: Force to add path in system env.
        False: Onluy add to system env if not exist.

    """
    # Set the logger
    set_logger(verbose=verbose)

    if (dirpath not in os.environ["PATH"]) or force:
        logger.info(f'Set ffmpeg path [{dirpath}] in system environment')
        os.environ["PATH"] += os.pathsep + dirpath
    else:
        logger.info(f'Path [{dirpath}] found in system environment')


# %%
def remove(dirpath, remove_dir: bool = False, verbose: [str, int] = 'info'):
    """Set directory to system path.

    Parameters
    ----------
    dirpath : String, optional
        Pathname of directory to save ffmpeg files.
        None: System temp directory
    verbose : [str, int], optional
        Set the verbose messages using string or integer values.

    """
    # Set the logger
    set_logger(verbose=verbose)

    if dirpath in os.environ["PATH"]:
        logger.info(f'Removing ffmpeg path [{dirpath}] from system environment')
        paths = os.environ["PATH"].split(os.pathsep)
        # Remove dirpath
        paths = [p for p in paths if p != dirpath]
        os.environ["PATH"] = os.pathsep.join(paths)
    else:
        logger.debug(f'Path [{dirpath}] not found in system environment')


    # Remove the directory and all its contents
    if remove_dir and os.path.exists(dirpath) and os.path.isdir(dirpath):
        logger.info(f'Deleting directory [{dirpath}]')
        shutil.rmtree(dirpath)


# %%
def printe():
    paths = os.environ["PATH"].split(os.pathsep)
    for path in paths:
        logger.info(f'{path}')

# %%
def extract_pathnames(dirpath, gfile):
    idx = gfile[::-1].find('.') + 1
    dirname = gfile[:-idx]
    getPath = os.path.abspath(os.path.join(dirpath, dirname))
    getZip = os.path.abspath(os.path.join(dirpath, gfile))
    pathname, _ = os.path.split(getZip)
    getPath = os.path.join(pathname, dirname)

    # Matches _1, _10, _123, etc. at the end of the string
    pattern = r'_\d+$'
    # Check if the pattern matches
    if re.search(pattern, getPath):
        getPath = re.sub(pattern, '', getPath)

    return getPath, getZip

# %%
def extract_files(dirpath, gfile):
    logger.info('Extracting..')
    # Get pathnames
    extractionPath, getZip = extract_pathnames(dirpath, gfile)
    # Get ext
    ext = os.path.splitext(getZip)[1]

    # Unzip if path does not exists
    if os.path.isfile(getZip) and ext == '.zip':
        zip_ref = zipfile.ZipFile(getZip, 'r')
        zip_ref.extractall(dirpath)
        # zip_contents = zip_ref.namelist()
        zip_ref.close()
        # Remove zipfile
        os.remove(getZip)
    else:
        logger.error('Not a valid extension. Only .zip files can be processed.')

    return extractionPath


# %%
def get_platform():
    platforms = {
        'linux1':'linux',
        'linux2':'linux',
        'darwin':'osx',
        'win32':'windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    logger.debug(f'System found: {platforms[sys.platform]}')
    return platforms[sys.platform]


# %%
def get_setpath(dirpath):
    if dirpath is None:
        dirpath = os.path.join(tempfile.gettempdir(), 'ffmpeg')
    elif dirpath == 'workingdir':
        dirpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ffmpeg')

    if not os.path.isdir(dirpath):
        logger.info(f'Create ffmpeg directory: {dirpath}')
        os.makedirs(dirpath, exist_ok=True)

    # Return
    return dirpath


# %% Import example dataset from github.
def download_package(URL, dirpath, force_download=False):
    """Import example dataset from github.

    Parameters
    ----------
    URL : str, optional
        URL-Link to ffmpeg.
        default: 'https://erdogant.github.io//packages/ffmpeg-2025-03-06-git-696ea1c223-full_build.7z'
        latest: 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z'
    dirpath : String, optional
        Pathname of directory to save ffmpeg files.
        None: System temp directory

    Returns
    -------
    tuple : (gfile, dirpath).
        gfile : filename
        dirpath : currentpath

    """
    # Get zipfile
    gfile = wget.filename_from_url(URL)
    # Get full path to zipfile
    zipfilepath = os.path.join(dirpath, gfile)

    # Check if file exists
    if not os.path.isfile(zipfilepath) or force_download:
        # Download data from URL
        logger.info(f'Downloading ffmpeg {gfile}..')
        wget.download(URL, dirpath)
    else:
        logger.debug(f'[{gfile}] >Skip because found on disk.')

    # Return
    return gfile


# %% Retrieve files files.
class wget:
    """Retrieve file from URL."""

    def filename_from_url(URL):
        """Return filename."""
        return os.path.basename(URL)

    def download(URL, writepath):
        """Download.

        Parameters
        ----------
        URL : str.
            Internet source.
        writepath : str.
            Directory to write the file.

        Returns
        -------
        None.

        """
        filename = wget.filename_from_url(URL)
        # Ensure the directory exists
        os.makedirs(os.path.dirname(writepath), exist_ok=True)
        writepath = os.path.join(writepath, filename)
        # Set the folder to write mode (read, write, and execute)
        r = requests.get(URL, stream=True)
        # Check for HTTP errors (e.g., 404, 500)
        r.raise_for_status()
        # Write to disk
        with open(writepath, "wb") as fd:
            for chunk in r.iter_content(chunk_size=1024):
                fd.write(chunk)

# %%
def get_logger():
    return logger.getEffectiveLevel()


# %%
def set_logger(verbose: [str, int] = 'info'):
    """Set the logger for verbosity messages.

    Parameters
    ----------
    verbose : [str, int], default is 'info' or 20
        Set the verbose messages using string or integer values.
        * [0, 60, None, 'silent', 'off', 'no']: No message.
        * [10, 'debug']: Messages from debug level and higher.
        * [20, 'info']: Messages from info level and higher.
        * [30, 'warning']: Messages from warning level and higher.
        * [50, 'critical']: Messages from critical level and higher.

    Returns
    -------
    None.

    > # Set the logger to warning
    > set_logger(verbose='warning')
    > # Test with different messages
    > logger.debug("Hello debug")
    > logger.info("Hello info")
    > logger.warning("Hello warning")
    > logger.critical("Hello critical")

    """
    # Set 0 and None as no messages.
    if (verbose==0) or (verbose is None):
        verbose=60
    # Convert str to levels
    if isinstance(verbose, str):
        levels = {'silent': 60,
                  'off': 60,
                  'no': 60,
                  'debug': 10,
                  'info': 20,
                  'warning': 30,
                  'error': 50,
                  'critical': 50}
        verbose = levels[verbose]

    # Show examples
    logger.setLevel(verbose)


# %% Main
if __name__ == "__main__":
    pass
