import os

from PIL import Image, ImageDraw, ImageFont


def create_banner():
    # Dimensions for Open Graph
    width, height = 1200, 630

    # Colors (Dark Theme with Cyan/Blue)
    bg_color = (15, 23, 42)  # Dark Blue/Slate
    accent_color = (6, 182, 212)  # Cyan
    text_color = (255, 255, 255)  # White

    # Create image
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Draw simple geometric accents (Futuristic lines)
    draw.rectangle([0, 0, width, 10], fill=accent_color)
    draw.rectangle([0, height - 10, width, height], fill=accent_color)
    draw.line([0, 0, 200, height], fill=(30, 41, 59), width=100)

    # Load Font (Default to simple if specific not found, but try to use a system font)
    try:
        # Try finding a nice font, or fallback to default
        font_title = ImageFont.truetype("arial.ttf", 80)
        font_sub = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Text - Title
    title = "AutoRewardsPC"
    # Calculate text size (rudimentary for default font compatibility)
    bbox_title = draw.textbbox((0, 0), title, font=font_title)
    w_title = bbox_title[2] - bbox_title[0]
    h_title = bbox_title[3] - bbox_title[1]

    draw.text(
        ((width - w_title) / 2, (height / 2) - 60),
        title,
        font=font_title,
        fill=text_color,
    )

    # Text - Subtitle
    subtitle = "Automated Microsoft Rewards System"
    bbox_sub = draw.textbbox((0, 0), subtitle, font=font_sub)
    w_sub = bbox_sub[2] - bbox_sub[0]

    draw.text(
        ((width - w_sub) / 2, (height / 2) + 40),
        subtitle,
        font=font_sub,
        fill=accent_color,
    )

    # Save
    output_path = os.path.join("assets", "social_preview.png")
    img.save(output_path)
    print(f"Social preview created at: {output_path}")


if __name__ == "__main__":
    create_banner()
