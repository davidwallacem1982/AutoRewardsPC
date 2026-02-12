import os

from PIL import Image, ImageOps


def create_social_preview_from_manual():
    # Source image from manual extraction
    source_path = os.path.join("assets", "extracted_from_manual", "image2.png")
    output_path = os.path.join("assets", "social_preview.png")

    if not os.path.exists(source_path):
        print(f"Error: Source image not found at {source_path}")
        return

    # Target dimensions
    target_width, target_height = 1200, 630
    bg_color = (15, 23, 42)  # Dark Blue/Slate background

    try:
        img = Image.open(source_path)

        # Create background
        background = Image.new("RGB", (target_width, target_height), bg_color)

        # Calculate aspect ratios
        img_ratio = img.width / img.height
        target_ratio = target_width / target_height

        # Logic to fit image nicely
        # If image is taller than target (relativistically), fit to height
        # If image is wider, fit to width
        # But we want to ensure it's contained and centered

        # Resize image to fit within target dimensions (contain)
        # using ImageOps.contain or manual calculation
        # New width/height calculation:

        if img_ratio > target_ratio:
            # Width limited
            new_width = target_width
            new_height = int(target_width / img_ratio)
        else:
            # Height limited
            new_height = target_height
            new_width = int(target_height * img_ratio)

        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Center position
        x_offset = (target_width - new_width) // 2
        y_offset = (target_height - new_height) // 2

        # Paste resized image onto background
        background.paste(resized_img, (x_offset, y_offset))

        # Save
        background.save(output_path)
        print(f"Created social preview at {output_path}")
        print(f"Derived from {source_path} (original: {img.width}x{img.height})")

    except Exception as e:
        print(f"Failed to create social preview: {e}")


if __name__ == "__main__":
    create_social_preview_from_manual()
