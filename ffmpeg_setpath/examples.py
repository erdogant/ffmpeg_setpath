# %%
# import ffmpeg_setpath
# print(dir(ffmpeg_setpath))
# print(ffmpeg_setpath.__version__)

# %%
from ffmpeg_setpath import ffmpeg_setpath
# ffmpeg_setpath(dirpath=r'c:/ffmpeg/')
ffmpeg_setpath()

# %% Force to set path in env
import ffmpeg_setpath
ffmpeg_setpath.set_path(r'c:/temp/ffmpeg/')

# %% Remove specified path from env
import ffmpeg_setpath
ffmpeg_setpath.remove(r'c:\ffmpeg\bin')

# %% Show all paths in env
import ffmpeg_setpath
ffmpeg_setpath.printe()

