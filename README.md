📋 Setup Instructions
1. Create GitHub Repository
bash
# Create new repository on GitHub first, then:
git clone https://github.com/yourusername/grassbot-telegram
cd grassbot-telegram

# Add all files
git add .

# Initial commit
git commit -m "Initial GrassBot deployment with Telegram control"

# Push to GitHub
git push origin main
2. Railway Deployment
Go to Railway.app and connect your GitHub repository

Set environment variables in Railway dashboard:

TELEGRAM_BOT_TOKEN: From @BotFather

ADMIN_CHAT_IDS: Your Telegram chat ID (get from @userinfobot)

Deploy automatically

3. Telegram Bot Commands Usage
Command	Example	Function
/start_farming	/start_farming	Start farming with all user IDs
/update_proxies	/update_proxies http://proxy1:port	Update proxy list
Send JSON	Direct message with JSON	Update config.json
🔧 Key Features
Complete Telegram Control: All functions accessible via Telegram commands

Dynamic Configuration: Update config and proxies via Telegram

Railway Deployment: Ready for cloud deployment

Error Handling: Comprehensive error handling and logging

Security: Admin-only access control


# 🤖 GrassBot with Telegram Control

A powerful automated farming system for Grass with remote control via Telegram bot. Deploy on Railway for 24/7 operation.

![GitHub](https://img.shields.io/badge/python-3.8%2B-blue)
![Telegram](https://img.shields.io/badge/Telegram-Bot-green)
![Railway](https://img.shields.io/badge/Deploy-Railway-purple)

## 🚀 Features

- **Telegram Bot Control**: Manage everything via Telegram commands
- **Dynamic Configuration**: Update user IDs and proxies remotely
- **Railway Deployment**: Easy cloud deployment
- **Proxy Support**: Rotating proxy support for better performance
- **Multi-User Support**: Handle multiple user accounts simultaneously
- **Real-time Monitoring**: Get status updates via Telegram

## 📋 Prerequisites

- Python 3.8+
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- Railway account (for deployment)
- Grass user IDs and device IDs

## 🛠️ Setup Instructions

### 1. Create Telegram Bot

1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Use `/newbot` command to create a new bot
3. Save the API token provided
4. Get your Chat ID by messaging [@userinfobot](https://t.me/userinfobot)

### 2. Repository Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/grassbot-telegram
cd grassbot-telegram

🤖 Telegram Bot Commands
Command	Description	Example
/start	Start the bot and show help	/start
/status	Check bot status and statistics	/status
/start_farming	Start the farming process	/start_farming
/stop_farming	Stop the farming process	/stop_farming
/update_proxies	Update proxy list	/update_proxies http://proxy1:port
/update_config	Update configuration	/update_config {"user_ids": ["id1"]}
/view_config	View current configuration	/view_config
/view_proxies	View current proxies	/view_proxies
/restart	Restart the bot	/restart
/help	Show detailed help	/help
🔄 Updating Configuration via Telegram
Method 1: Direct command

text
/update_config {"user_ids": ["id1", "id2"], "settings": {"ping_interval": 30}}
Method 2: Send JSON message
Simply send the JSON configuration as a direct message to the bot.

Method 3: Update proxies

text
/update_proxies http://proxy1:3129 http://proxy2:3129
Or reply to a message containing proxies with /update_proxies

📁 Project Structure
text
grassbot-telegram/
├── main.py              # Main application entry point
├── bot_controller.py    # Telegram bot handlers
├── grassbot_core.py     # GrassBot core logic
├── config.json          # User IDs configuration
├── devices.json         # Device IDs storage
├── proxy.txt           # Proxy list
├── requirements.txt    # Python dependencies
├── railway.json       # Railway configuration
├── nixpacks.toml      # Build configuration
├── Procfile           # Process definition
├── .gitignore         # Git ignore rules
└── README.md          # This file
🔧 Manual Installation (Optional)
If you want to run locally instead of Railway:

bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export TELEGRAM_BOT_TOKEN="your_bot_token"
export ADMIN_CHAT_IDS='["your_chat_id"]'

# Run the application
python main.py
⚙️ Environment Variables
Variable	Required	Description
TELEGRAM_BOT_TOKEN	Yes	Your Telegram bot token
ADMIN_CHAT_IDS	Yes	JSON array of admin chat IDs
CONFIG_FILE	No	Path to config file (default: config.json)
DEVICE_FILE	No	Path to devices file (default: devices.json)
PROXY_FILE	No	Path to proxy file (default: proxy.txt)
🐛 Troubleshooting
Common Issues
Bot not responding

Check if TELEGRAM_BOT_TOKEN is correct

Verify ADMIN_CHAT_IDS contains your chat ID

Deployment fails on Railway

Check requirements.txt for syntax errors

Verify all required files are in repository

Farming not starting

Check config.json has valid user IDs

Verify devices.json has device IDs

Ensure proxy.txt has valid proxies (if using proxies)

Logs and Monitoring
Check Railway logs for detailed error information. The bot will send status updates to Telegram for monitoring.

🤝 Contributing
Fork the repository

Create a feature branch

Commit your changes

Push to the branch

Create a Pull Request

📄 License
This project is for educational purposes only. Use at your own risk.

⚠️ Disclaimer
This software is provided for educational purposes only. Users are responsible for complying with terms of service of any platforms they interact with.

📞 Support
For issues and questions:

Check the troubleshooting section above

Review Railway deployment logs

Ensure all configuration files are properly formatted


Yes, exactly! You can run it in Termux on your Android device or in terminal on your PC - the code works the same way locally as it does on Railway.

📱 Running in Termux (Android)
Step 1: Install Termux
Download Termux from Google Play Store or F-Droid

Open Termux

Step 2: Setup in Termux
bash
# Update packages
pkg update && pkg upgrade

# Install Python and git
pkg install python git

# Clone your repository
git clone https://github.com/yourusername/grassbot-telegram
cd grassbot-telegram

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export TELEGRAM_BOT_TOKEN="your_actual_bot_token"
export ADMIN_CHAT_IDS='["your_actual_chat_id"]'

# Run the bot
python main.py
💻 Running on PC/Laptop
Windows (Command Prompt/PowerShell):
bash
# Clone repository
git clone https://github.com/yourusername/grassbot-telegram
cd grassbot-telegram

# Install dependencies
pip install -r requirements.txt

# Set environment variables (Windows CMD)
set TELEGRAM_BOT_TOKEN=your_actual_bot_token
set ADMIN_CHAT_IDS=["your_actual_chat_id"]

# Run
python main.py
Windows (PowerShell):
powershell
$env:TELEGRAM_BOT_TOKEN="your_actual_bot_token"
$env:ADMIN_CHAT_IDS='["your_actual_chat_id"]'
python main.py
Linux/Mac:
bash
git clone https://github.com/yourusername/grassbot-telegram
cd grassbot-telegram
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN="your_actual_bot_token"
export ADMIN_CHAT_IDS='["your_actual_chat_id"]'
python main.py
🔄 Same Code, Different Environments
The code works identically in all environments:

✅ Railway: 24/7 cloud hosting (recommended)

✅ Termux: Run on your Android phone

✅ PC/Laptop: Run on your computer

✅ VPS: Run on a virtual private server

⚖️ Pros and Cons:
Railway (Cloud) - Recommended
✅ 24/7 operation (runs even when your phone is off)

✅ No battery drain

✅ Better reliability

❌ Requires deployment setup

Termux (Local on Phone)
✅ Easy to test

✅ Immediate control

❌ Only runs when Termux is open

❌ Drains phone battery

❌ Internet connection required

PC (Local on Computer)
✅ Good for development

✅ Easy to debug

❌ Only runs when computer is on

❌ Not 24/7 unless you leave PC running

🎯 Recommended Approach:
Start with Railway deployment first - get it running in the cloud for 24/7 operation.

Then test locally in Termux to make sure everything works and for quick testing.

📱 Termux Specific Tips:
bash
# Keep Termux running in background
termux-wake-lock

# Install additional useful packages
pkg install termux-api termux-tools

# Run in background (even when app closed)
# Use Termux:Widget or third-party apps to keep it running
🔧 Environment Variables Permanent Setup:
For local running, you can create a .env file (but don't upload to GitHub):

Create .env file in your project folder:

env
TELEGRAM_BOT_TOKEN=your_actual_bot_token_here
ADMIN_CHAT_IDS=["your_actual_chat_id_here"]
Then modify main.py to load from .env:

python
from dotenv import load_dotenv
load_dotenv()  # Add this at the top of main.py
🚀 Quick Test in Termux:
If you want to test quickly:

Install Termux

Run the commands above

See if bot starts without errors

Then deploy to Railway for 24/7 operation

✅ Bottom Line:
Yes, the same exact code works everywhere! You can:

Test locally in Termux (quick and easy)

Deploy to Railway for 24/7 operation (recommended for production)

Which one do you want to try first? I recommend starting with Railway deployment since your GitHub repository is already complete! 🚀

