import os

from PIL import Image


def optimize_assets(directory="assets"):
    """Optimizes PNG and JPG images in the given directory."""
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    print(f"Optimizing assets in '{directory}'...")

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                filepath = os.path.join(root, file)
                try:
                    img = Image.open(filepath)
                    original_size = os.path.getsize(filepath)

                    # Save with optimization
                    if file.lower().endswith(".png"):
                        img.save(filepath, optimize=True, compress_level=9)
                    else:
                        img.save(filepath, optimize=True, quality=85)

                    new_size = os.path.getsize(filepath)
                    saved = original_size - new_size
                    if saved > 0:
                        print(f"  Optimized {file}: Saved {saved} bytes")
                    else:
                        print(f"  {file} already optimized")

                except Exception as e:
                    print(f"  Could not optimize {file}: {e}")


if __name__ == "__main__":
    optimize_assets()
