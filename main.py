from src.moviepy.animation.wave import wave_animation
from src.util.split_text import split_text
from moviepy import *
import numpy as np

text_for_video = ("Questo è un esempio di un testo molto lungo che vogliamo dividere in più segmenti "
             "in modo da visualizzarlo pezzo per pezzo sul video. Ogni segmento verrà mostrato per una parte "
             "della durata totale del video, in maniera sequenziale.")

def generate_video(text_segments):
    clip = VideoFileClip("assets/background_video/barbazza.mp4")
    clip = clip.resized(height=1920).cropped(width=1080, x_center=clip.w)
    
    duration_per_segment = clip.duration / len(text_segments)
    animated_text_clips = []
    
    for i, segment in enumerate(text_segments):
        test_var = wave_animation(time=duration_per_segment, font_path='assets/font/Roboto-Black.ttf', fontsize=70, text=segment, spacing=5)
        animated_text_clip = VideoClip(test_var, duration=duration_per_segment)
        animated_text_clip = animated_text_clip.with_position(("center", 500))
        animated_text_clip = animated_text_clip.with_start(i * duration_per_segment)
        animated_text_clips.append(animated_text_clip)
    
    final_clip = CompositeVideoClip([clip] + animated_text_clips, size=clip.size)
    final_clip.write_videofile("assets/output/barbazza_dynamic_color_wave.mp4", codec='libx264', fps=25)

text_split = split_text(text_for_video, max_words_per_segment=3)
generate_video(text_segments=text_split)