import logging
from emoji import emojize
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os
from dotenv import load_dotenv


load_dotenv()


logging.basicConfig(filename="bot.log", 
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def get_smile():
    smile = emojize("😃")
    return smile


def main_keyboard():
    return ReplyKeyboardMarkup([['/help', 'Тест']])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f"Здравствуйте, {user_name}! {get_smile()}",
                                    reply_markup=main_keyboard())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # chat_id = update.effective_chat.id
    # await context.bot.send_photo(chat_id=chat_id, photo=open('cats.jpg', 'rb'))
    await update.message.reply_text("Help!",
                                    reply_markup=main_keyboard())


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text,
                                    reply_markup=main_keyboard())


def main() -> None:
    application = Application.builder().token(os.getenv("TOKEN")).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()


if __name__ == "__main__":
    main()