from content_generator import ContentGenerator
from telegram_publisher import TelegramPublisher
from config import Config

def main():
    # Load and validate config
    config = Config()
    config.validate()

    print("username: ",config.TELEGRAM_CHANNEL_USERNAME)
    
    # Initialize services
    generator = ContentGenerator(config.GEMINI_API_KEY)
    publisher = TelegramPublisher(config.TELEGRAM_BOT_TOKEN, config.TELEGRAM_CHANNEL_ID)
    
    try:
        # Generate content
        content = generator.generate_content(config.TELEGRAM_CHANNEL_USERNAME)
        
        # Publish to Telegram
        publisher.publish_post(content)
        print("Successfully published daily post!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()