from moviepy.editor import *
import os
from natsort import natsorted

path = os.walk("/home/finesto/Documents/Torrents/[GigaCourse.Com] Udemy - Complete Python Developer in 2022 Zero to Mastery/04 - Python Basics II/")

L = []

for root, dirs, files in path:
    files = natsorted(files)
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)

final_clip = concatenate_videoclips(L)
final_clip.to_videofile(path + "output.mp4", fps=24, remove_temp=False)

# from pathlib import Path
# from moviepy.editor import *
# import ffmpeg

# path = Path('/home/finesto/Documents/Torrents/[GigaCourse.Com] Udemy - Complete Python Developer in 2022 Zero to Mastery/04 - Python Basics II')

# fileList = sorted(path.glob('*.mp4'))

# for file in fileList:
#     print(file)

# ffmpeg.input(fileList).concat(str(fileList[0]), str(fileList[1])).output('output.mp4').run()

# # i = 0
# # clip = []
# # for file in fileList:
# #     if (fileList[i] is None):
# #         break
# #     clip.append(VideoFileClip(str(fileList[i])))
# #     ++i

# # final = concatenate_videoclips(clip)
# # final.write_videofile("merged.mp4")

# # In case small number of videos to concatenate
# # clip1 = VideoFileClip(str(fileList[0]))
# # clip2 = VideoFileClip(str(fileList[1]))

# # final = concatenate_videoclips([clip1, clip2])
# # final.write_videofile("merged.mp4")
