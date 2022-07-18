from moviepy.editor import VideoFileClip, vfx

clip1 = VideoFileClip("test.mp4")

clip1 = clip1.fx(vfx.resize, width=100)

clip1.write_videofile("test.mp4")
