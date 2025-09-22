import os
import asyncio
import json
import aiofiles
from grassbot_core import GrassBotCore
from bot_controller import TelegramBotController

class MainApplication:
    def __init__(self):
        self.grassbot = None
        self.telegram_bot = None
        self.is_running = True
        
    async def initialize(self):
        """Initialize all components"""
        print("🚀 Initializing GrassBot Application...")
        
        # Initialize GrassBot core
        self.grassbot = GrassBotCore()
        
        # Initialize Telegram bot controller
        self.telegram_bot = TelegramBotController(self.grassbot)
        
        # Load initial configuration
        await self.grassbot.load_config()
        await self.grassbot.load_devices()
        
        print("✅ Application initialized successfully")
    
    async def start_all_services(self):
        """Start all services concurrently"""
        tasks = []
        
        # Start Telegram bot
        if self.telegram_bot:
            tasks.append(asyncio.create_task(self.telegram_bot.start_bot()))
        
        # Start GrassBot farming
        tasks.append(asyncio.create_task(self.start_farming()))
        
        # Wait for all tasks
        await asyncio.gather(*tasks, return_exceptions=True)
    
    async def start_farming(self):
        """Start the farming process"""
        await asyncio.sleep(5)  # Wait for Telegram bot to initialize
        if self.grassbot:
            await self.grassbot.start_farming_process()
    
    async def shutdown(self):
        """Graceful shutdown"""
        self.is_running = False
        if self.telegram_bot:
            await self.telegram_bot.shutdown()
        if self.grassbot:
            await self.grassbot.shutdown()

async def main():
    app = MainApplication()
    
    try:
        await app.initialize()
        await app.start_all_services()
        
        # Keep the application running
        while app.is_running:
            await asyncio.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Received shutdown signal...")
    except Exception as e:
        print(f"❌ Fatal error: {e}")
    finally:
        await app.shutdown()

if __name__ == "__main__":
    asyncio.run(main())