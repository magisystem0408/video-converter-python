from moviepy.editor import *

clip = VideoFileClip("test.mp4")

print(clip.w)
print(clip.h)
print(clip.size)
print(clip.duration)
print(clip.fps)
