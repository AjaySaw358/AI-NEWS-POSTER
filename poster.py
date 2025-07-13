import json
import os
from utils import get_today_filename, clear_output
from generate_carousel import create_carousel
from post_to_instagram_and_facebook import post_carousel

def post_daily_carousels():
    filename = get_today_filename()

    if not os.path.exists(filename):
        print(f"❌ News file not found: {filename}")
        return

    with open(filename, "r", encoding="utf-8") as f:
        news_data = json.load(f)

    # Iterate through categories (e.g. AI, Finance, Crypto)
    for category, articles in news_data.items():
        print(f"\n🎨 Creating post for: {category}")

        # Create carousel slides: images with 3-5 news pieces
        image_paths = create_carousel(category, articles)

        if not image_paths:
            print(f"⚠️ No images created for {category}")
            continue

        # Combine slide captions for social post
        caption = f"🌍 {category} Highlights\n\nFollow for daily insights!\n#news #dailyupdates #ai #tech"

        # Upload carousel to FB/IG
        post_carousel(image_paths, caption)

    # Cleanup
    os.remove(filename)
    clear_output()
    print("\n✅ All done. News posted and files cleared!")

if __name__ == "__main__":
    post_daily_carousels()
