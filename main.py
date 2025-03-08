from moviepy import *

text_for_video = ("Questo è un esempio di un testo molto lungo che vogliamo dividere in più segmenti "
             "in modo da visualizzarlo pezzo per pezzo sul video. Ogni segmento verrà mostrato per una parte "
             "della durata totale del video, in maniera sequenziale.")

def generate_video(text):
    clip = VideoFileClip("assets/background_video/barbazza.mp4")
    clip_resized = clip.resized(height=1920).cropped(width=1080, x_center=clip.w)
    #clip_vertical = clip_resized.cropped(clip_resized, width=1080, x_center=clip_resized.w/2)
    segment_duration = clip.duration / len(text)

    # Crea una lista di TextClip per ciascun segmento, impostando la durata e il tempo di inizio
    text_clips = []
    for i, seg in enumerate(text):
        txt_clip = TextClip(text=seg, 
                            font="assets/font/Roboto-Black.ttf",
                            font_size=70,
                            color='black') \
                   .with_duration(segment_duration) \
                   .with_position("center") \
                   .with_start(segment_duration * i)
        text_clips.append(txt_clip)
        
    final_clip = CompositeVideoClip([clip_resized, *text_clips], size=(1080, 1920))

    final_clip.write_videofile("assets/output/barbazza.mp4", codec='libx264', fps=25)

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

text_split = split_text(text_for_video)
generate_video(text=text_split)