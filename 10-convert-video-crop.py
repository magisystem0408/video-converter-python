from moviepy.editor import VideoFileClip, vfx

clip1 = VideoFileClip("test.mp4")

clip1 = clip1.fx(vfx.crop, x1=100, x2=40, y1=200, y2=300)

clip1.write_videofile("test.mp4")
