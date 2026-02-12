import os

from PIL import Image, ImageDraw


def create_icon(name, draw_func, color="white", size=(64, 64)):
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw, size, color)

    # Save
    path = os.path.join("assets", "icons", f"{name}.png")
    img.save(path)
    print(f"Generated {path}")


def draw_play(draw, size, color):
    # Triangle pointing right
    w, h = size
    points = [
        (w * 0.3, h * 0.2),  # Top Left
        (w * 0.3, h * 0.8),  # Bottom Left
        (w * 0.8, h * 0.5),  # Right
    ]
    draw.polygon(points, fill=color)


def draw_stop(draw, size, color):
    # Square
    w, h = size
    m = w * 0.25
    draw.rectangle([m, m, w - m, h - m], fill=color)


def draw_target(draw, size, color):
    # Crosshair / Circle
    w, h = size
    cx, cy = w / 2, h / 2
    r = w * 0.35
    # Main ring
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=4)
    # Inner dot
    r_dot = w * 0.05
    draw.ellipse([cx - r_dot, cy - r_dot, cx + r_dot, cy + r_dot], fill=color)
    # Cross lines
    m = w * 0.1
    draw.line([cx, m, cx, h - m], fill=color, width=3)
    draw.line([m, cy, w - m, cy], fill=color, width=3)


def draw_notebook(draw, size, color):
    # Logs / Document
    w, h = size
    m = w * 0.2
    # Page
    draw.rectangle([m, m * 0.5, w - m, h - m * 0.5], outline=color, width=3)
    # Lines
    line_x_start = m * 1.5
    line_x_end = w - m * 1.5
    for i in range(1, 4):
        y = m * 0.5 + (h - m) * (i / 4.0)
        draw.line([line_x_start, y, line_x_end, y], fill=color, width=3)


def draw_upload(draw, size, color):
    # Arrow Up
    w, h = size
    cx = w / 2
    # Arrow head
    points = [
        (cx, h * 0.2),  # Top
        (w * 0.2, h * 0.5),  # Left
        (w * 0.8, h * 0.5),  # Right
    ]
    draw.polygon(points, fill=color)
    # Stem
    draw.rectangle([cx - w * 0.1, h * 0.5, cx + w * 0.1, h * 0.8], fill=color)


def draw_download(draw, size, color):
    # Arrow Down
    w, h = size
    cx = w / 2
    # Arrow head (pointing down)
    points = [
        (cx, h * 0.8),  # Bottom
        (w * 0.2, h * 0.5),  # Left
        (w * 0.8, h * 0.5),  # Right
    ]
    draw.polygon(points, fill=color)
    # Stem
    draw.rectangle([cx - w * 0.1, h * 0.2, cx + w * 0.1, h * 0.5], fill=color)


def draw_save(draw, size, color):
    w, h = size
    m = w * 0.2
    # Box
    draw.rectangle([m, m, w - m, h - m], outline=color, width=4)
    # Inner part
    draw.rectangle([m + w * 0.1, m + h * 0.1, w - m - w * 0.1, m + h * 0.3], fill=color)


def draw_cancel(draw, size, color):
    w, h = size
    m = w * 0.25
    # X
    draw.line([m, m, w - m, h - m], fill=color, width=5)
    draw.line([m, h - m, w - m, m], fill=color, width=5)


if __name__ == "__main__":
    if not os.path.exists(os.path.join("assets", "icons")):
        os.makedirs(os.path.join("assets", "icons"))

    # Theme Colors mapping (approximate from theme.py)
    # Start: White (on Green)
    create_icon("play", draw_play, color="white")

    # Stop: White (on Red)
    create_icon("stop", draw_stop, color="white")

    # Calibrate: Cyan (Text is Cyan, button Transparent)
    # Or maybe white is safer? Theme.SECONDARY is #00D4FF
    create_icon("target", draw_target, color="#00D4FF")

    # Logs: White (on Slate Grey)
    create_icon("logs", draw_notebook, color="white")

    # Import: White (on Dark Blue)
    create_icon("import", draw_upload, color="white")

    # Export: Black (on Light Blue #29B6F6)
    create_icon("export", draw_download, color="black")

    # --- New Icons for Calibration ---
    # Save: Black (on Cyan Theme.SECONDARY)
    # floppy disk or checkmark
    create_icon("save", draw_save, color="black")

    # Cancel: Red (#FF4B4B) (on Transparent)
    create_icon("cancel", draw_cancel, color="#FF4B4B")  # Theme.DANGER

    # Capture: White (on Green Theme.PRIMARY) - Reuse Target shape but white
    create_icon("capture", draw_target, color="white")

    print("Icons created successfully.")
