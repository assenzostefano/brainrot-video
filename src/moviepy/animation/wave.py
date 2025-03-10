from PIL import Image, ImageDraw, ImageFont
import numpy as np
import colorsys

def make_frame(t, font_path, fontsize, text, spacing):
    # Load the font
    fontsize = int(fontsize)
    font = ImageFont.truetype(font_path, fontsize)
    widths, text_height = get_text_dimensions(text, font)
    total_width = sum(widths) + spacing * (len(text) - 1)
    
    img = Image.new("RGBA", (total_width, text_height + 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    x = 0
    for i, char in enumerate(text):
        if char == " ":
            x += widths[i] + spacing
            continue
        hue = (t * 0.5 + i / len(text)) % 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        r, g, b = int(r * 255), int(g * 255), int(b * 255)
        y_offset = int(20 * np.sin(2 * np.pi * (i / len(text) + t)))
        draw.text((x, y_offset), char, font=font, fill=(r, g, b, 255))
        x += widths[i] + spacing
    return np.array(img)

# Function to calculate the size of each character
def get_text_dimensions(text, font):
    # Use font.getbbox to get the width of each character
    widths = [font.getbbox(char)[2] - font.getbbox(char)[0] for char in text]
    height = font.getbbox(text)[3] - font.getbbox(text)[1]
    return widths, height

def wave_animation(time, font_path, fontsize, text, spacing):
    return lambda t: make_frame(t, font_path, fontsize, text, spacing)