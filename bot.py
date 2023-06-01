import logging
from handlers import start_command, help_command, echo, get_image
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv


load_dotenv()


logging.basicConfig(filename="bot.log", 
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main() -> None:
    application = Application.builder().token(os.getenv("TOKEN")).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command)) 
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(MessageHandler(filters.PHOTO, get_image))
    application.run_polling()


if __name__ == "__main__":
    main()