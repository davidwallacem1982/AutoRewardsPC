import os

from PIL import Image


def list_image_dimensions(directory, output_file="dimensions.txt"):
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    print(f"Checking images in {directory}...")
    results = []
    for filename in os.listdir(directory):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            filepath = os.path.join(directory, filename)
            try:
                with Image.open(filepath) as img:
                    width, height = img.size
                    info = f"{filename}: {width}x{height} ({os.path.getsize(filepath)} bytes)"
                    print(info)
                    results.append(info)
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    with open(output_file, "w") as f:
        f.write("\n".join(results))


if __name__ == "__main__":
    list_image_dimensions("assets/extracted_from_manual")
