import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler
from config import TELEGRAM_API_KEY, WEB_APP_URL

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update, context):
    # Create the "Let's Start" button
    keyboard = [[InlineKeyboardButton("Let's Start", url=WEB_APP_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the message with the button
    await update.message.reply_text('Click the button below to start:', reply_markup=reply_markup)

def main():
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TELEGRAM_API_KEY).build()
    
    # Register the start command handler
    application.add_handler(CommandHandler("start", start))
    
    # Log all errors
    application.add_error_handler(lambda update, context: logger.error(f"An error occurred: {context.error}"))
    
    # Start the bot
    application.run_polling(timeout=100)  # Set timeout here
    logger.info("Bot is starting...")

if __name__ == '__main__':
    main()
