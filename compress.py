from PIL import Image
import os

def compress_image(input_path, output_path, quality=30):
    img = Image.open(input_path)
    img.save(output_path, "JPEG", optimize=True, quality=quality)
    return output_path
  
