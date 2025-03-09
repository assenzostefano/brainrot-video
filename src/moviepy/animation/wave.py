from PIL import Image, ImageDraw, ImageFont
import numpy as np
import colorsys

def wave_animation(font_path, fontsize, text, spacing, t):
    # Load the font
    font = ImageFont.truetype(font_path, fontsize)

    # Function to calculate the dimensions of each character
    widths, text_height = get_text_dimensions(text, font)
    total_width = sum(widths) + spacing * (len(text) - 1)

    # Create transparent image with dimensions suitable for text
    img = Image.new("RGBA", (total_width, text_height + 50), (0, 0, 0, 0))  # Aggiungi spazio per l'onda
    draw = ImageDraw.Draw(img)
    x = 0

    # For each letter, draw the character with a color that changes over time
    for i, char in enumerate(text):
        # Se è uno spazio, aggiungi un offset e continua
        if char == " ":
            x += widths[i] + spacing
            continue
        # Calcola l'hue dinamico: varia con il tempo e in base all'indice della lettera
        hue = (t * 1 + i / len(text)) % 1.0  # modificando il moltiplicatore (qui 0.5) si velocizza o rallenta il cambiamento
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        r, g, b = int(r * 255), int(g * 255), int(b * 255)
        # Calcola l'offset verticale per l'effetto onda
        y_offset = int(20 * np.sin(2 * np.pi * (i / len(text) + t)))
        # Disegna il carattere con il colore calcolato e l'offset verticale
        draw.text((x, y_offset), char, font=font, fill=(r, g, b, 255))
        x += widths[i] + spacing
    return np.array(img)

# Funzione per calcolare le dimensioni di ciascun carattere
def get_text_dimensions(text, font):
    # Usa font.getbbox per ottenere la larghezza di ogni carattere
    widths = [font.getbbox(char)[2] - font.getbbox(char)[0] for char in text]
    height = font.getbbox(text)[3] - font.getbbox(text)[1]
    return widths, height


def make_frame(time):
    return wave_animation(font_path="assets/font/Roboto-Black.ttf", fontsize=70, text="Prova in stile onda", spacing=5, t=time)
