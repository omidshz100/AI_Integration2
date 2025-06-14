# AI Integration - OpenRouter Chat

A simple command-line chat application that connects to the OpenRouter.ai API, allowing you to interact with various AI models directly from your terminal.

## Features

- 🤖 Interactive command-line chat interface
- 🔄 Conversation history maintained throughout the session
- 🔐 Secure API key management using environment variables
- ⚡ Fast responses with configurable timeout
- 🛡️ Comprehensive error handling
- 🎯 Uses DeepSeek R1 model (free tier)

## Prerequisites

- Python 3.6 or higher
- OpenRouter.ai API key (get one at [https://openrouter.ai/keys](https://openrouter.ai/keys))

## Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd AI_Integration
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   Create a `.env` file in the project root and add your OpenRouter API key:
   ```env
   OPENROUTER_API_KEY=your_actual_api_key_here
   ```
   
   **Important:** Never commit your actual API key to version control!

## Usage

1. **Run the chat application**
   ```bash
   python openrouter_chat.py
   ```

2. **Start chatting**
   - Type your message and press Enter
   - The AI will respond with generated text
   - Conversation history is maintained throughout the session

3. **Exit the application**
   - Type `exit` or `quit` to end the conversation
   - Use `Ctrl+C` to interrupt at any time

## Configuration

The application uses the following default settings:

- **Model:** `deepseek/deepseek-r1-0528-qwen3-8b:free`
- **Temperature:** 0.7 (controls randomness)
- **Max Tokens:** 1000 (maximum response length)
- **Timeout:** 30 seconds

You can modify these settings by editing the configuration variables in `openrouter_chat.py`.

## Project Structure

```
AI_Integration/
├── openrouter_chat.py    # Main chat application
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (API key)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Dependencies

- **requests** (>=2.25.0): For making HTTP requests to the OpenRouter API
- **python-dotenv** (>=0.19.0): For loading environment variables from .env file

## Error Handling

The application includes comprehensive error handling for:

- ❌ Network connection issues
- ⏱️ Request timeouts
- 🔑 Invalid API keys
- 📝 Malformed API responses
- 🚫 API rate limits and errors

## Security Notes

- ✅ API keys are loaded from environment variables
- ✅ No hardcoded credentials in the source code
- ✅ `.env` file should be added to `.gitignore`
- ⚠️ Never share your API key publicly

## Troubleshooting

### Common Issues

1. **"OPENROUTER_API_KEY environment variable is not set"**
   - Make sure you have created a `.env` file with your API key
   - Verify the API key format is correct

2. **Connection errors**
   - Check your internet connection
   - Verify the OpenRouter API is accessible

3. **API errors**
   - Ensure your API key is valid and has sufficient credits
   - Check if you've exceeded rate limits

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## License

This project is open source. Please check the license file for more details.

## Acknowledgments

- [OpenRouter.ai](https://openrouter.ai/) for providing the AI API
- [DeepSeek](https://www.deepseek.com/) for the AI model

---

**Happy chatting! 🚀**