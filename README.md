# WhatsApp ChatGPT AI Chatbot in Python 🤖

**A general-purpose, customizable WhatsApp AI Chatbot in Python 🐍 that can understand text 📝, audio 🎵 and images 🖼️, and reply your clients 💬** about anything related to your business 🏢 directly on WhatsApp ✅. Powered by OpenAI GPT4o 🚀 (other models can be used too) and [Wassenger WhatsApp API](https://wassenger.com) 🔗.

**Now supports GPT-4o with text + audio + image input 📝🎵🖼️, audio responses 🔊**, and improved RAG with MCP tools 🛠️ and external functions for external API calls support 🌐

Find other AI Chatbot implementations in [Node.js](https://github.com/wassengerhq/whatsapp-chatgpt-bot) and [PHP](https://github.com/wassengerhq/whatsapp-chatgpt-bot-php)

🚀 **[Get started for free with Wassenger WhatsApp API](https://wassenger.com/register)** in minutes by connecting your existing WhatsApp number and [obtain your API key](https://app.wassenger.com/apikeys) ✨

## Features

- 🤖 **Fully featured chatbot** for your WhatsApp number connected to Wassenger
- 💬 **Automatic replies** to incoming messages from users
- 🌍 **Multi-language support** - understands and replies in 90+ different languages
- 🎤 **Audio input/output** - transcription and text-to-speech capabilities
- 🖼️ **Image processing** - can analyze and understand images
- 👥 **Human handoff** - allows users to request human assistance
- ⚙️ **Customizable AI behavior** and instructions
- 🔧 **Function calling** capabilities for external data integration
- 📊 **Memory management** with conversation history and rate limiting
- 🚦 **Smart routing** with webhook handling and error management
- 🔒 **Secure** with proper error handling and logging

## Contents
- [Features](#features)
- [Quick Start](#quick-start)
- [Requirements](#requirements)
- [Configuration](#configuration)
  - [API Keys Setup](#api-keys-setup)
  - [Bot Customization](#bot-customization)
- [Usage](#usage)
  - [Local Development](#local-development)
  - [Production Deployment](#production-deployment)
- [Deployment](#deployment)
- [Architecture](#architecture)
- [Testing](#testing)
- [Development](#development)
- [Customization](#customization)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/wassengerhq/whatsapp-chatgpt-bot-python.git
   cd whatsapp-chatgpt-bot-python
   ```
2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env file with your API keys (see Configuration section)
   ```
4. **Run the bot (development mode):**
   ```bash
   uvicorn src.main:app --reload --port 8080
   # Or use provided scripts for Ngrok tunnel
   ```

## Requirements

- Python 3.9 or higher
- [WhatsApp](https://whatsapp.com) Personal or Business number
- [Wassenger API key](https://app.wassenger.com/developers/apikeys) - [Sign up for free](https://wassenger.com/register)
- [OpenAI API key](https://platform.openai.com/account/api-keys) - Sign up for free
- [Ngrok](https://ngrok.com) account (for local development) - [Sign up for free](https://dashboard.ngrok.com/signup)

## Configuration

Edit the `.env` file with your API credentials:

```bash
# Required: Wassenger API key
API_KEY=your_wassenger_api_key_here

# Required: OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here

# OpenAI model to use (gpt-4o, gpt-4, gpt-3.5-turbo)
OPENAI_MODEL=gpt-4o

# Required for local development: Ngrok auth token
NGROK_TOKEN=your_ngrok_token_here

# Optional: Specific WhatsApp device ID
DEVICE=

# Optional: Webhook URL for production deployment
WEBHOOK_URL=https://yourdomain.com/webhook

# Server configuration
PORT=8080
LOG_LEVEL=info
```

### API Keys Setup

1. **Wassenger API Key**:
   - Sign up at [Wassenger](https://app.wassenger.com)
   - Go to [API Keys](https://app.wassenger.com/developers/apikeys)
   - Create a new API key and copy it to `API_KEY` in `.env`

2. **OpenAI API Key**:
   - Sign up at [OpenAI](https://platform.openai.com)
   - Go to [API Keys](https://platform.openai.com/account/api-keys)
   - Create a new API key and copy it to `OPENAI_API_KEY` in `.env`

3. **Ngrok Token** (for local development):
   - Sign up at [Ngrok](https://ngrok.com)
   - Get your auth token from the dashboard
   - Copy it to `NGROK_TOKEN` in `.env`

### Bot Customization

Edit `src/config/bot_config.py` to customize:
- Bot instructions and personality
- Welcome and help messages
- Supported features (audio, images, etc.)
- Rate limits and quotas
- Whitelisted/blacklisted numbers
- Labels and metadata settings

## Usage

### Local Development

1. Start the development server:
   ```bash
   uvicorn src.main:app --reload --port 8080
   ```
2. The bot will:
   - Start a local HTTP server on port 8080
   - Optionally create an Ngrok tunnel automatically
   - Register the webhook with Wassenger
   - Begin processing WhatsApp messages

3. Send a message to your WhatsApp number connected to Wassenger to test the bot.

### Production Deployment

1. Set environment variables on your server:
   ```bash
   export WEBHOOK_URL=https://yourdomain.com/webhook
   export API_KEY=your_wassenger_api_key
   export OPENAI_API_KEY=your_openai_api_key
   ```
2. Deploy to your web server (e.g., Gunicorn/Uvicorn, Docker, or cloud platform)
3. Make sure your server can receive POST requests at `/webhook`

## Deployment

You can deploy this bot to any cloud platform that supports Python and FastAPI. Example (Docker):

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

## Architecture

The Python implementation follows a modern, modular architecture:

```
src/
├── api/         # API clients (OpenAI, Wassenger)
├── bot/         # Core bot logic (ChatBot, FunctionHandler)
├── config/      # Configuration management
├── http/        # HTTP routing and webhook handling
├── storage/     # In-memory storage
├── utils/       # Utilities (logging, Ngrok)
└── main.py      # FastAPI app entrypoint
```

## Testing

The project includes several test utilities to validate your setup:

- **Configuration Test**: Validate that all configuration files load correctly and dependencies are installed.
- **API Connection Test**: Test connectivity to Wassenger and OpenAI APIs with your configured keys.
- **Webhook Test**: Simulate a webhook request to test the message processing pipeline.

Example (using HTTPie):
```bash
http POST http://localhost:8080/webhook event=message:in:new data:='{"chat": {"id": "test", "fromNumber": "123", "type": "chat"}, "fromNumber": "123", "body": "Hello"}'
```

## Development

### Project Structure

```
chatgpt-python/
├── src/
│   ├── api/           # API integrations
│   ├── bot/           # Core bot logic
│   ├── config/        # Configuration
│   ├── http/          # HTTP handling
│   ├── storage/       # Data storage
│   ├── utils/         # Utility classes
│   └── main.py        # FastAPI app entry point
├── tests/             # Test utilities
├── .env.example       # Environment template
├── requirements.txt   # Python dependencies
└── README.md
```

### Key Classes
- **`ChatBot`** - Main bot processing logic
- **`OpenAIClient`** - OpenAI API integration with chat, audio, and image support
- **`WassengerClient`** - Wassenger API integration for WhatsApp messaging
- **`FunctionHandler`** - AI function calling system
- **`Router`** - HTTP request routing and webhook handling
- **`BotConfig`** - Centralized configuration management
- **`MemoryStore`** - In-memory caching and conversation state management
- **`AppLogger`** - Logging system
- **`NgrokTunnel`** - Development tunneling

### Customization

#### Bot Instructions
Edit the AI behavior in `src/config/bot_config.py`:
```python
BOT_INSTRUCTIONS = 'You are a helpful assistant...'
```

#### Function Calling
Add custom functions in `src/bot/function_handler.py`:
```python
def get_business_hours():
    return {
        'monday': '9:00 AM - 6:00 PM',
        'tuesday': '9:00 AM - 6:00 PM',
        # ... more days
    }
```

#### Rate Limits
Adjust limits in `src/config/bot_config.py`:
```python
LIMITS = {
    'maxInputCharacters': 1000,
    'maxOutputTokens': 1000,
    'chatHistoryLimit': 20,
    # ... more limits
}
```

## API Endpoints

- `GET /` - Bot information and status
- `POST /webhook` - Webhook for incoming WhatsApp messages
- `POST /message` - Send message endpoint
- `GET /sample` - Send sample message
- `GET /files/{id}` - Temporary file downloads

## Troubleshooting

### Common Issues

1. **"No active WhatsApp numbers"**
   - Verify your Wassenger API key
   - Check that you have a connected WhatsApp device in Wassenger

2. **"WhatsApp number is not online"**
   - Ensure your WhatsApp device is connected and online in Wassenger dashboard

3. **Webhook not receiving messages**
   - Check that your webhook URL is accessible from the internet
   - Verify Ngrok tunnel is running (development mode)
   - Check firewall settings

4. **OpenAI API errors**
   - Verify your OpenAI API key is valid
   - Check your OpenAI account has sufficient credits
   - Ensure the model name is correct

### Debug Mode

Enable detailed logging by setting in `.env`:
```bash
LOG_LEVEL=debug
```

Then check the logs in your console or configured log output.

## Resources

- [Wassenger Documentation](https://app.wassenger.com/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pyngrok Documentation](https://pyngrok.readthedocs.io/en/latest/)
- [GitHub Issues](https://github.com/wassengerhq/whatsapp-chatgpt-bot-python/issues)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

---

Built with ❤️ using Python and the Wassenger API.
