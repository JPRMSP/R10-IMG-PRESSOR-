from PIL import Image
import os

def compress_image(input_path, output_path, quality=30):
    """
    Compresses an image and saves it to the given output path.

    Parameters:
    - input_path (str): Path to the original image.
    - output_path (str): Path to save the compressed image.
    - quality (int): Quality of the output image (1 to 95).
                     Lower means more compression and smaller file size.

    Returns:
    - output_path (str): Path to the compressed image.
    """
    try:
        # Open the image
        img = Image.open(input_path)

        # Convert image to RGB if it’s in another mode (e.g., RGBA or P)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Save the image in JPEG format with specified quality
        img.save(output_path, "JPEG", optimize=True, quality=quality)
        return output_path

    except Exception as e:
        print(f"Error compressing image: {e}")
        return None
