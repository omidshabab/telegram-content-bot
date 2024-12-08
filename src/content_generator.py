import google.generativeai as genai
import os
from typing import Dict, Any

class ContentGenerator:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
    def generate_content(self, channel_username: str, topics: str) -> Dict[str, Any]:
        prompt = f"""
        Create a short, engaging post in Persian about one of these topics: {topics}.
        The post should:
        - Be direct and start with the main content (no greetings)
        - Use a friendly tone
        - Include relevant emojis
        - Be maximum 10 sentences
        - Focus on practical insights or tips
        - Don't include any hashtags
        """
        
        response = self.model.generate_content(prompt)
        
        # Ensure we get a response
        if not response.text:
            raise Exception("Failed to generate content")
        
        content_with_channel = f"{response.text}\n\n@{channel_username}"
            
        return {
            "content": content_with_channel,
        }