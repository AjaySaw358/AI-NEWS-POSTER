import os
import json
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from utils import get_today_filename, ensure_output_dir

# ==== 🔧 SETTINGS ====
SLIDE_WIDTH = 1080
SLIDE_HEIGHT = 1080
MARGIN = 60
TITLE_FONT_SIZE = 54
TEXT_FONT_SIZE = 42
FINAL_SLIDE_FONT_SIZE = 48

# Use built-in Mac font path (Arial or Helvetica)
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"  # Or Helvetica
BACKGROUND_COLOR = (245, 245, 245)
TEXT_COLOR = (0, 0, 0)
BRAND_COLOR = (30, 144, 255)  # Dodger Blue for attention

LOGO_BOX = True  # Show placeholder logo box

# ==== 📦 LOAD NEWS ====
def load_news():
    filename = get_today_filename()
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

# ==== 🎨 CREATE SLIDE ====
def create_slide(text, index, total, is_final=False):
    img = Image.new("RGB", (SLIDE_WIDTH, SLIDE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(FONT_PATH, FINAL_SLIDE_FONT_SIZE if is_final else TITLE_FONT_SIZE)
    text_font = ImageFont.truetype(FONT_PATH, TEXT_FONT_SIZE)

    y = MARGIN

    # Optional logo box
    if LOGO_BOX:
        draw.rectangle([SLIDE_WIDTH - 180, 20, SLIDE_WIDTH - 60, 140], outline=BRAND_COLOR, width=3)
        draw.text((SLIDE_WIDTH - 165, 60), "LOGO", font=text_font, fill=BRAND_COLOR)

    # Add text (wrap manually)
    lines = []
    words = text.split()
    line = ""

    for word in words:
        test_line = f"{line} {word}".strip()
        if draw.textlength(test_line, font=text_font) < (SLIDE_WIDTH - 2 * MARGIN):
            line = test_line
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)

    for line in lines:
        draw.text((MARGIN, y), line, font=text_font, fill=TEXT_COLOR)
        y += TEXT_FONT_SIZE + 10

    # Page number
    page_text = f"{index+1}/{total}"
    draw.text((SLIDE_WIDTH - 120, SLIDE_HEIGHT - 70), page_text, font=text_font, fill=(100, 100, 100))

    return img

# ==== 🖼️ GENERATE ALL CAROUSELS ====
def generate_carousel():
    ensure_output_dir()
    news_data = load_news()
    output_folder = "output"
    count = 0

    for category, articles in news_data.items():
        for article in articles:
            count += 1
            slides = []

            # Slide 1: Title
            slides.append(create_slide(article["title"], 0, 4))

            # Slide 2: Summary
            slides.append(create_slide(article["summary"], 1, 4))

            # Slide 3: "Read more" link
            slides.append(create_slide(f"Read full article:\n{article['link']}", 2, 4))

            # Slide 4: Final message
            ending_text = (
                "Follow @dailyinsights_diva for more updates!\n"
                "💬 These are automated news summaries. No harm or offense is intended."
            )
            slides.append(create_slide(ending_text, 3, 4, is_final=True))

            # Save as separate images (or combine later into carousel)
            for i, slide in enumerate(slides):
                fname = os.path.join(output_folder, f"post_{count}_slide_{i+1}.jpg")
                slide.save(fname)
                print(f"✅ Saved {fname}")

if __name__ == "__main__":
    generate_carousel()
