import logging
import subprocess
from telegram import Update
from update_jellyfin import update_jellyfin_library
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set your Telegram bot token here
TOKEN = ""

# Set the path to your download.py script
DOWNLOAD_SCRIPT_PATH = "download.py"
update_SCRIPT_PATH = "update_jellyfin.py"

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the /start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('/download then link')
    
def update(update: Update, context: CallbackContext) -> None:
    try:
            # Execute the download.py script with the user's message as an argument
            subprocess.run(['python3',update_SCRIPT_PATH], check=True, capture_output=True, text=True)

            # Send a success message
            update.message.reply_text(f'playlist update started')
    except subprocess.CalledProcessError as e:
            # Send an error message if the script execution fails
            update.message.reply_text(f'Error: {e.stderr}')
    

# Define the /download command handler
def download(update: Update, context: CallbackContext) -> None:
    # Check if the command is sent with a message
    if context.args:
        # Get the user's message and strip whitespaces
        user_message = ' '.join(context.args).strip()
        
        if "&&" in user_message:
            pass
        else:
            try:
                # Execute the download.py script with the user's message as an argument
                subprocess.run(['python3', DOWNLOAD_SCRIPT_PATH, user_message], check=True, capture_output=True, text=True)

                # Send a success message
                update.message.reply_text(f'Success! The song/playlist were added')
            except subprocess.CalledProcessError as e:
                # Send an error message if the script execution fails
                update.message.reply_text(f'Error: {e.stderr}')
    else:
        # Reply with an error message if no message is provided
        update.message.reply_text('Unknown options. Please provide a message with the /download command.')

# Define the message handler
def echo(update: Update, context: CallbackContext) -> None:
    # Reply with an error message for unknown commands
    update.message.reply_text('Unknown command. Type /start to begin.')

# Define the main function
def main() -> None:
    # Create the Updater and pass it the bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the /start command handler
    dp.add_handler(CommandHandler("start", start))

    # Register the /download command handler
    dp.add_handler(CommandHandler("download", download))

    # Register the /download command handler
    dp.add_handler(CommandHandler("update", update))
    
    # Register the message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
