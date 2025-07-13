from datetime import datetime
import os

def get_today_filename():
    return f"daily_news_{datetime.today().strftime('%Y-%m-%d')}.json"

def clear_output():
    if os.path.exists("output"):
        for file in os.listdir("output"):
            os.remove(os.path.join("output", file))
