from moviepy.editor import *

"""映像の回転"""
video = VideoFileClip("test.mp4").rotate(90)


video.write_videofile("video-convert-rotate.mp4")