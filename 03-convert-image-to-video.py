from moviepy.editor import *

clip = ImageSequenceClip(["image1.jpg", "image2.jpg"], fps=0.1)


clip.write_videofile("test.mp4")
