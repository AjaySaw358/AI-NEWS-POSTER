import feedparser
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

rss_feeds = {
    "Tech & Startups": "https://www.theverge.com/rss/index.xml",
    "Crypto & Web3": "https://decrypt.co/feed",
    "Finance & Markets": "https://www.investing.com/rss/news_25.rss",
    "AI & Tools": "https://venturebeat.com/category/ai/feed/",
    "Global Business News": "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best"
}

news_data = {}
for sector, url in rss_feeds.items():
    print(f"\n📡 Fetching: {sector}")
    feed = feedparser.parse(url)
    print(f" - Found {len(feed.entries)} articles")
    
    articles = []
    for entry in feed.entries[:5]:
        print(f"   📰 {entry.title}")
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published if "published" in entry else "N/A"
        })
    
    news_data[sector] = articles

timestamp = datetime.now().strftime("%Y-%m-%d")
filename = f"daily_news_{timestamp}.json"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(news_data, f, indent=4)

print(f"\n✅ News saved to {filename}")