def split_text(text, max_words_per_segment=3):
    """
    Divides the text into segments, each containing at most max_words_per_segment words.
    """
    words = text.split()
    segments = []
    for i in range(0, len(words), max_words_per_segment):
        segment = " ".join(words[i:i+max_words_per_segment])
        segments.append(segment)
    return segments