from moviepy.editor import *

clip = VideoFileClip("test.mp4")

# 3秒に縮める
clip = clip.subclip(0, 3)

clip.write_gif("convert-gif-video.gif")
