from telegram import Update
from telegram.ext import ContextTypes
from utils import get_smile, main_keyboard


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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