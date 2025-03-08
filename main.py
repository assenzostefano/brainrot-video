from moviepy import *

clip = VideoFileClip("assets/background_video/barbazza.mp4").subclipped(50,60)

txt_clip = TextClip(text="Prova", font="assets/font/Roboto-Black.ttf", font_size=70, color='white') \
           .with_duration(10) \
           .with_position("center")

final_clip = CompositeVideoClip([clip, txt_clip], size=(1920, 1080))

final_clip.write_videofile("assets/output/barbazza.mp4", codec='libx264', fps=25)