# src/telegram_publisher.py
import requests
from typing import Dict, Any

class TelegramPublisher:
    def __init__(self, bot_token: str, channel_id: str):
        self.bot_token = bot_token
        self.channel_id = channel_id
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
        
    def publish_post(self, content: str) -> bool:
        endpoint = f"{self.base_url}/sendMessage"
        
        data = {
            "chat_id": self.channel_id,
            "text": content,
            "parse_mode": "HTML"
        }
        
        response = requests.post(endpoint, data=data)
        
        if not response.ok:
            raise Exception(f"Failed to publish post: {response.text}")
            
        return True