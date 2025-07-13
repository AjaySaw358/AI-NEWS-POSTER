import os
import requests
from dotenv import load_dotenv

load_dotenv()

IG_PAGE_ID = os.getenv("INSTAGRAM_PAGE_ID")
FB_PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

def upload_image_to_fb(image_path, caption):
    url = f"https://graph.facebook.com/v20.0/{FB_PAGE_ID}/photos"
    with open(image_path, "rb") as image_file:
        response = requests.post(url, data={
            "caption": caption,
            "access_token": ACCESS_TOKEN
        }, files={"source": image_file})
    print("📤 FB Upload:", response.json())

def upload_image_to_ig(image_path, caption):
    url = f"https://graph.facebook.com/v20.0/{IG_PAGE_ID}/media"
    image_url = "https://yourpublicimagehost.com/image.jpg"  # <-- We'll replace this later with actual hosting or leave IG posting optional for now
    data = {
        "image_url": image_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }
    print("🚧 IG Upload Placeholder: Implement upload method")

def post_all():
    for file in sorted(os.listdir("output")):
        if file.endswith(".png"):
            path = os.path.join("output", file)
            caption = "Your Daily News Dose by @dailyinsights_diva"
            upload_image_to_fb(path, caption)
    print("✅ All images posted.")
