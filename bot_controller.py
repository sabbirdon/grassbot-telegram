import os
import json
import aiofiles
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

class TelegramBotController:
    def __init__(self, grassbot_instance):
        self.grassbot = grassbot_instance
        self.app = None
        self.bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
        self.admin_chat_ids = json.loads(os.environ.get('ADMIN_CHAT_IDS', '[]'))
        
    async def start_bot(self):
        """Initialize and start the Telegram bot"""
        if not self.bot_token:
            print("❌ Telegram bot token not configured")
            return
            
        try:
            self.app = Application.builder().token(self.bot_token).build()
            
            # Set up command handlers
            await self.setup_commands()
            
            print("✅ Telegram bot started successfully")
            await self.app.run_polling()
            
        except Exception as e:
            print(f"❌ Error starting Telegram bot: {e}")
    
    async def setup_commands(self):
        """Setup bot commands and handlers"""
        commands = [
            BotCommand("start", "Start the bot"),
            BotCommand("status", "Check bot status"),
            BotCommand("start_farming", "Start farming process"),
            BotCommand("stop_farming", "Stop farming process"),
            BotCommand("update_proxies", "Update proxy list"),
            BotCommand("update_config", "Update configuration"),
            BotCommand("view_config", "View current configuration"),
            BotCommand("view_proxies", "View current proxies"),
            BotCommand("restart", "Restart bot"),
            BotCommand("help", "Show help message")
        ]
        
        await self.app.bot.set_my_commands(commands)
        
        # Add command handlers
        self.app.add_handler(CommandHandler("start", self.start_command))
        self.app.add_handler(CommandHandler("status", self.status_command))
        self.app.add_handler(CommandHandler("start_farming", self.start_farming_command))
        self.app.add_handler(CommandHandler("stop_farming", self.stop_farming_command))
        self.app.add_handler(CommandHandler("update_proxies", self.update_proxies_command))
        self.app.add_handler(CommandHandler("update_config", self.update_config_command))
        self.app.add_handler(CommandHandler("view_config", self.view_config_command))
        self.app.add_handler(CommandHandler("view_proxies", self.view_proxies_command))
        self.app.add_handler(CommandHandler("restart", self.restart_command))
        self.app.add_handler(CommandHandler("help", self.help_command))
        
        # Add message handler for JSON updates
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
    
    async def verify_admin(self, update: Update) -> bool:
        """Verify if user is admin"""
        user_id = str(update.effective_user.id)
        if user_id not in self.admin_chat_ids:
            await update.message.reply_text("❌ Unauthorized access. You are not an admin.")
            return False
        return True
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        if not await self.verify_admin(update):
            return
            
        welcome_text = """
🤖 *GrassBot Control Panel*

*Available Commands:*
/start - Show this message
/status - Check bot status
/start_farming - Start farming process
/stop_farming - Stop farming process
/update_proxies - Update proxy list
/update_config - Update configuration
/view_config - View current configuration
/view_proxies - View current proxies
/restart - Restart bot
/help - Show detailed help

*Quick Setup:*
1. Add your proxy list to proxy.txt or use /update_proxies
2. Configure your user IDs in config.json or use /update_config
3. Start farming with /start_farming

Send JSON configuration directly to update config.
        """
        await update.message.reply_text(welcome_text, parse_mode='Markdown')
    
    async def start_farming_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start_farming - Main farming command"""
        if not await self.verify_admin(update):
            return
            
        try:
            if self.grassbot:
                await self.grassbot.start_farming_process()
                
                # Get status information
                config = await self.grassbot.load_config()
                devices = await self.grassbot.load_devices()
                
                status_info = f"""
✅ *Farming Started Successfully*

• 👥 Users: {len(config.get('user_ids', []))}
• 📱 Devices: {len(devices.get('device_ids', []))}
• 🔄 Proxies: {len(self.grassbot.current_proxies) if hasattr(self.grassbot, 'current_proxies') else 'Loading...'}
• 🏃 Status: Active
                """
                await update.message.reply_text(status_info, parse_mode='Markdown')
            else:
                await update.message.reply_text("❌ GrassBot core not initialized")
                
        except Exception as e:
            await update.message.reply_text(f"❌ Error starting farming: {str(e)}")
    
    async def update_proxies_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /update_proxies command"""
        if not await self.verify_admin(update):
            return
            
        try:
            if context.args:
                # Parse proxies from command arguments
                proxies_text = ' '.join(context.args)
                proxies_list = [p.strip() for p in proxies_text.split() if p.strip()]
                
                await self.update_proxy_file(proxies_list)
                await update.message.reply_text(f"✅ Updated proxy list with {len(proxies_list)} proxies")
                
            elif update.message.reply_to_message and update.message.reply_to_message.text:
                # Parse proxies from replied message
                replied_text = update.message.reply_to_message.text
                proxies_list = [p.strip() for p in replied_text.split('\n') if p.strip() and p.startswith('http')]
                
                if proxies_list:
                    await self.update_proxy_file(proxies_list)
                    await update.message.reply_text(f"✅ Updated proxy list with {len(proxies_list)} proxies from replied message")
                else:
                    await update.message.reply_text("❌ No valid proxies found in replied message")
            else:
                help_text = """
📋 *How to update proxies:*

*Option 1: Command arguments*
`/update_proxies http://proxy1:port http://proxy2:port`

*Option 2: Reply to a message*
1. Send your proxy list (one per line)
2. Reply to that message with `/update_proxies`

*Option 3: File upload*
Send a .txt file with proxies
                """
                await update.message.reply_text(help_text, parse_mode='Markdown')
                
        except Exception as e:
            await update.message.reply_text(f"❌ Error updating proxies: {str(e)}")
    
    async def update_config_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /update_config command"""
        if not await self.verify_admin(update):
            return
            
        try:
            if context.args:
                config_text = ' '.join(context.args)
                new_config = json.loads(config_text)
                
                await self.update_config_file(new_config)
                user_count = len(new_config.get('user_ids', []))
                await update.message.reply_text(f"✅ Config updated with {user_count} user IDs")
            else:
                await update.message.reply_text(
                    "Please provide JSON config. Example:\n"
                    "`/update_config {\"user_ids\": [\"id1\", \"id2\"]}`",
                    parse_mode='Markdown'
                )
                
        except json.JSONDecodeError:
            await update.message.reply_text("❌ Invalid JSON format")
        except Exception as e:
            await update.message.reply_text(f"❌ Error updating config: {str(e)}")
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle direct JSON messages for config updates"""
        if not await self.verify_admin(update):
            return
            
        try:
            new_config = json.loads(update.message.text)
            
            if 'user_ids' in new_config:
                await self.update_config_file(new_config)
                user_count = len(new_config['user_ids'])
                await update.message.reply_text(f"✅ Config updated with {user_count} user IDs from message")
            else:
                await update.message.reply_text("❌ JSON must contain 'user_ids' field")
                
        except json.JSONDecodeError:
            # Not a JSON message, ignore
            pass
    
    async def update_proxy_file(self, proxies_list):
        """Update proxy.txt file"""
        async with aiofiles.open('proxy.txt', 'w') as f:
            for proxy in proxies_list:
                await f.write(f"{proxy}\n")
        
        # Update GrassBot's proxy list
        if self.grassbot:
            self.grassbot.current_proxies = set(proxies_list)
        
        print(f"Updated proxy list with {len(proxies_list)} entries")
    
    async def update_config_file(self, new_config):
        """Update config.json file"""
        # Merge with existing config
        try:
            async with aiofiles.open('config.json', 'r') as f:
                existing_config = json.loads(await f.read())
        except:
            existing_config = {}
        
        existing_config.update(new_config)
        
        async with aiofiles.open('config.json', 'w') as f:
            await f.write(json.dumps(existing_config, indent=2))
        
        print(f"Config updated with {len(new_config.get('user_ids', []))} user IDs")
    
    async def shutdown(self):
        """Shutdown the bot"""
        if self.app:
            await self.app.shutdown()

# Additional helper functions would be here...