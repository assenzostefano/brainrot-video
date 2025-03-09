from PIL import Image, ImageDraw, ImageFont
import numpy as np
import colorsys

def make_frame(font_path, fontsize, text, spacing, t):
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
        # If it is a space, add an offset and continue
        if char == " ":
            x += widths[i] + spacing
            continue
        # Calculates dynamic hue: varies with time and according to letter index
        hue = (t * 1 + i / len(text)) % 1.0  # Changing the multiplier (here 0.5) speeds up or slows down the change
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        r, g, b = int(r * 255), int(g * 255), int(b * 255)
        # Calculates the vertical offset for the wave effect
        y_offset = int(20 * np.sin(2 * np.pi * (i / len(text) + t)))
        # Draw the font with the calculated colour and vertical offset
        draw.text((x, y_offset), char, font=font, fill=(r, g, b, 255))
        x += widths[i] + spacing
    return np.array(img)

# Function to calculate the size of each character
def get_text_dimensions(text, font):
    # Use font.getbbox to get the width of each character
    widths = [font.getbbox(char)[2] - font.getbbox(char)[0] for char in text]
    height = font.getbbox(text)[3] - font.getbbox(text)[1]
    return widths, height

def wave_animation(time):
    return make_frame(font_path="assets/font/Roboto-Black.ttf", fontsize=70, text="Prova in stile onda", spacing=5, t=time)