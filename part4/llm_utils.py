import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "models/gemini-flash-lite-latest"

URL = f"https://generativelanguage.googleapis.com/v1beta/{MODEL}:generateContent?key={API_KEY}"


def call_llm(system_prompt,
             user_prompt,
             temperature=0,
             max_tokens=512):

    headers = {
        "Content-Type": "application/json"
    }

    payload = {

        "system_instruction": {
            "parts": [
                {
                    "text": system_prompt
                }
            ]
        },

        "contents": [
            {
                "parts": [
                    {
                        "text": user_prompt
                    }
                ]
            }
        ],

        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens
        }

    }

    response = requests.post(
        URL,
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return None

    response_json = response.json()

    return response_json["candidates"][0]["content"]["parts"][0]["text"]