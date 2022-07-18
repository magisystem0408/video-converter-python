"""
generate video clip
"""

from moviepy.editor import *

clip = ColorClip(size=(320, 288), color=[255, 32, 32])

clip = clip.set_duration(5)

clip.fps = 24

clip.write_videofile("test.mp4")