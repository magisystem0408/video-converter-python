from moviepy.editor import VideoFileClip, clips_array

clip1 = VideoFileClip("test.mp4")
clip2 = VideoFileClip("test.mp4")

result = clips_array([clip2, clip1,
                      clip1, clip2
                      ])

result.write_videofile("image")
