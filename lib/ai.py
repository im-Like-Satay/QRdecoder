import os

import dotenv
from google import genai

from lib.prompt import prompt

dotenv.load_dotenv()


def aiParser(data):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=[
            prompt,
            data,
        ],
    )
    return {"response": response.text}
