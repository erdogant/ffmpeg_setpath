# %%
# import ffmpeg_setpath
# print(dir(ffmpeg_setpath))
# print(ffmpeg_setpath.__version__)

# %%
from ffmpeg_setpath import ffmpeg_setpath
# ffmpeg_setpath(dirpath=r'c:/ffmpeg/', force=False)
ffmpeg_setpath()


# %% Force to set path in env
import ffmpeg_setpath
ffmpeg_setpath.set_path(dirpath=r'c:/temp/ffmpeg/')

# %% Remove specified path from env
import ffmpeg_setpath
ffmpeg_setpath.remove(r'c:\ffmpeg1\bin')


# %% Show all paths in env
import ffmpeg_setpath
ffmpeg_setpath.printe()

#%%