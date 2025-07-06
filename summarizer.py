import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize(text, model="gpt-4"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "Summarize the following news:"},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()
