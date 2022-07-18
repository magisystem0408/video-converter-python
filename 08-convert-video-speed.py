from moviepy.editor import VideoFileClip, vfx

clip1 = VideoFileClip("test.mp4")

clip1 = clip1.fx(vfx.speedx, 0.5)

clip1.write_videofile("test.mp4")
