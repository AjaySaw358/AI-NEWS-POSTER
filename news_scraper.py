import feedparser
import json
from datetime import datetime
import os
from dotenv import load_dotenv
from summarizer import summarize  # ✅ Updated summarize function

load_dotenv()

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
        title = entry.title
        link = entry.link
        description = entry.get("summary", "")
        published = entry.published if "published" in entry else "N/A"

        print(f"   📰 {title}")
        summary = summarize(title, description)

        if not summary:
            summary = "⚠️ Summary unavailable."

        articles.append({
            "title": title,
            "link": link,
            "published": published,
            "summary": summary
        })

    news_data[sector] = articles

# Save the news to a timestamped JSON file
timestamp = datetime.now().strftime("%Y-%m-%d")
filename = f"daily_news_{timestamp}.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(news_data, f, indent=4, ensure_ascii=False)

print(f"\n✅ News saved to {filename}")
