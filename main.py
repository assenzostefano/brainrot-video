from src.moviepy.animation.wave import wave_animation

from src.util.split_text import split_text

from moviepy import *
import numpy as np
text_for_video = ("Questo è un esempio di un testo molto lungo che vogliamo dividere in più segmenti "
             "in modo da visualizzarlo pezzo per pezzo sul video. Ogni segmento verrà mostrato per una parte "
             "della durata totale del video, in maniera sequenziale.")

def generate_video(text):
    clip = VideoFileClip("assets/background_video/barbazza.mp4").subclipped(50, 60)
    clip = clip.resized(height=1920).cropped(width=1080, x_center=clip.w)
    
    # apply wave animation to text
    animated_text_clip = VideoClip(wave_animation, duration=10)  # duration in seconds
    # Position the text clip, e.g. in the horizontal centre and in a chosen vertical position
    animated_text_clip = animated_text_clip.with_position(("center", 500))
    animated_text_clip = animated_text_clip.with_duration(clip.duration)

    # Combine background video with animated text clip
    final_clip = CompositeVideoClip([clip, animated_text_clip], size=clip.size)

    # Export the final video
    final_clip.write_videofile("assets/output/barbazza_dynamic_color_wave.mp4", codec='libx264', fps=25)

text_split = "Prova in stile onda"
#text_split = split_text("Prova in stile onda")
generate_video(text=text_split)