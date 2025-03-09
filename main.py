from moviepy import *
import numpy as np
from src.moviepy.animation.wave import wave_animation, make_frame
text_for_video = ("Questo è un esempio di un testo molto lungo che vogliamo dividere in più segmenti "
             "in modo da visualizzarlo pezzo per pezzo sul video. Ogni segmento verrà mostrato per una parte "
             "della durata totale del video, in maniera sequenziale.")

def generate_video(text):
    clip = VideoFileClip("assets/background_video/barbazza.mp4").subclipped(50, 60)
    clip = clip.resized(height=1920).cropped(width=1080, x_center=clip.w)
    
    # Crea il clip testuale dinamico con make_frame
    animated_text_clip = VideoClip(make_frame, duration=10)  # durata in secondi
    # Posiziona il clip testuale, ad esempio al centro orizzontale e in una posizione verticale scelta (qui 500)
    animated_text_clip = animated_text_clip.with_position(("center", 500))
    animated_text_clip = animated_text_clip.with_duration(clip.duration)

    # Combina il video di sfondo con il clip testuale animato
    final_clip = CompositeVideoClip([clip, animated_text_clip], size=clip.size)

    # Esporta il video finale
    final_clip.write_videofile("assets/output/barbazza_dynamic_color_wave.mp4", codec='libx264', fps=25)

def split_text(text, max_words_per_segment=3):
    """
    Divide il testo in segmenti, ognuno contenente al massimo max_words_per_segment parole.
    """
    words = text.split()
    segments = []
    for i in range(0, len(words), max_words_per_segment):
        segment = " ".join(words[i:i+max_words_per_segment])
        segments.append(segment)
    return segments

text_split = "Prova in stile onda"
#text_split = split_text("Prova in stile onda")
generate_video(text=text_split)