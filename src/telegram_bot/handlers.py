import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
    user = update.effective_user
    logger.info(f"User {user.id} started the bot.")
    await update.message.reply_text(f"Hello, {user.first_name}! Welcome to the bot. How can I assist you today?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:    
    help_text = """
Available commands:
/start - Start the bot
/help - Show this help message
Just send me any message and I'll respond!
    """
    await update.message.reply_text(help_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
    user = update.effective_user
    user_message = update.message.text
    logger.info(f"Received message from {user.id}: {user_message}")
    response = f"You said: {user_message}"
    
    await update.message.reply_text(response)
    
async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Nice image! However, I can only process text messages at the moment.")
    
async def handle_unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Sorry, I didn't understand that command. Type /help to see available commands.")
        