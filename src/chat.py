from groq import Groq
from src.config import GROQ_API_KEY, MODEL_NAME, SYSTEM_PROMPT

import json
import os
from datetime import datetime

client = Groq(api_key=GROQ_API_KEY)


class ChatSession:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
    def send(self, user_input: str) -> str:
        self.messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=self.messages,
        )

        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})

        return reply
    def save(self) -> str:
        os.makedirs("conversations", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"conversations/chat_{timestamp}.json"

        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.messages, f, indent=2, ensure_ascii=False)

        return path

    