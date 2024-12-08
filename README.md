# Telegram Daily Post Generator

This project automates the generation and posting of daily content to a Telegram channel using the Google Generative AI model. It leverages environment variables for configuration and utilizes GitHub Actions for scheduling the daily post. The content is generated based on specified topics and is designed to be engaging and relevant to the audience.

## Project Structure

```
.
├── .github
│   └── workflows
│       └── daily_post.yml
├── src
│   ├── config.py
│   ├── content_generator.py
│   ├── main.py
│   └── telegram_publisher.py
├── requirements.txt
├── .env
├── .env.example
└── .gitignore
```

### File Descriptions

- **.github/workflows/daily_post.yml**: GitHub Actions workflow file that schedules the daily post generation and publishing.
- **src/config.py**: Configuration file that loads environment variables and validates their presence.
- **src/content_generator.py**: Contains the `ContentGenerator` class responsible for generating content using the Google Generative AI model.
- **src/main.py**: The main entry point of the application that orchestrates the content generation and publishing process.
- **src/telegram_publisher.py**: Contains the `TelegramPublisher` class that handles the posting of content to the Telegram channel.
- **requirements.txt**: Lists the Python dependencies required for the project.
- **.env**: Contains environment variables for API keys and configuration (not included in version control for security).
- **.env.example**: Example of the `.env` file structure for setting up environment variables.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## How to Use the Project

### Prerequisites

1. **Python 3.10 or higher**: Ensure you have Python installed on your machine.
2. **Google Generative AI API Key**: Obtain an API key from Google Cloud.
3. **Telegram Bot Token**: Create a Telegram bot and get the token.
4. **Telegram Channel ID**: Get the ID of the channel where you want to post.
5. **Set Up Environment Variables**: Create a `.env` file in the root directory based on the `.env.example` file.

### Steps to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Rename `.env.example` to `.env` and fill in the required values:
     ```plaintext
     GEMINI_API_KEY=your_gemini_api_key
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token
     TELEGRAM_CHANNEL_ID=your_channel_id
     TELEGRAM_CHANNEL_USERNAME=your_channel_username
     CONTENT_TOPICS="product management, indie hacking, or product design"
     ```

4. **Run the Application**:
   You can run the application manually using:
   ```bash
   python src/main.py
   ```

5. **Set Up GitHub Actions**:
   - Push your code to the `main` branch to trigger the GitHub Actions workflow, which will run the script daily at the specified time (9:30 UTC).

### Manual Trigger

You can also manually trigger the workflow from the GitHub Actions tab in your repository.

## Conclusion

This project provides a simple yet effective way to automate content generation and posting on Telegram. By leveraging the power of Google Generative AI and GitHub Actions, you can ensure consistent and engaging content for your audience.
