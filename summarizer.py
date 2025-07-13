import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize(title, description, model="gpt-4"):
    """Summarize a news article using OpenAI GPT."""
    text = f"Title: {title}\nDescription: {description}"

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Summarize this news in 2-3 sentences in a concise, engaging way."},
                {"role": "user", "content": text}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ Summarization error: {e}")
        return None
