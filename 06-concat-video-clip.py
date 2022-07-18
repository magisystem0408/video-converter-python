from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1 = VideoFileClip("test.mp4")
clip2 = VideoFileClip("test.mp4")

result = concatenate_videoclips([clip1, clip2])

result.write_videofile("concat-video-clip.mp4")
