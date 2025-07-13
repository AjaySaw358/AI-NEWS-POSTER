import feedparser
import json
from datetime import datetime
from dotenv import load_dotenv
import os
from summarizer import summarize
from utils import get_today_filename

load_dotenv()

rss_feeds = {
    "Tech & Startups": "https://www.theverge.com/rss/index.xml",
    "Crypto & Web3": "https://decrypt.co/feed",
    "Finance & Markets": "https://www.investing.com/rss/news_25.rss",
    "AI & Tools": "https://venturebeat.com/category/ai/feed/",
    "Global Business News": "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best"
}

def run_news_scraper():
    news_data = {}

    for sector, url in rss_feeds.items():
        print(f"\n📡 Fetching: {sector}")
        feed = feedparser.parse(url)
        print(f" - Found {len(feed.entries)} articles")

        articles = []

        for entry in feed.entries[:5]:  # limit per category
            title = entry.title
            link = entry.link
            description = entry.get("summary", "")
            published = entry.get("published", "N/A")

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

    filename = get_today_filename()
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(news_data, f, indent=4, ensure_ascii=False)

    print(f"\n✅ News saved to {filename}")
