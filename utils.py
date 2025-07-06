from datetime import datetime

def get_today_filename():
    return f"daily_news_{datetime.today().strftime('%Y-%m-%d')}.json"