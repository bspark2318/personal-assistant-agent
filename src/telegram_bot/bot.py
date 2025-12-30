import logging 
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters 
from src.config import Config 
from src.telegram_bot.handlers import start_command, help_command, handle_message, handle_image, handle_unknown

logger = logging.getLogger(__name__)

def create_bot() -> Application: 
    logger.info("Creating Telegram bot application")
    app = Application.builder().token(Config.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    app.add_handler(MessageHandler(filters.ALL, handle_unknown))
    
    logger.info("Telegram bot application created successfully")
    return app 

async def start_bot() -> None: 
    app = create_bot()
    logger.info("Starting Telegram bot")
    async with app: 
        await app.initialize()
        await app.start()
        await app.updater.start_polling()
        logger.info("Telegram bot started and polling for updates")
        
        import asyncio
        stop_event = asyncio.Event()
        await stop_event.wait()
    
