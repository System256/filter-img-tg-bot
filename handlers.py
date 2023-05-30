from telegram import Update
from telegram.ext import ContextTypes
from utils import get_smile, main_keyboard
from pathlib import Path


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f"Здравствуйте, {user_name}! {get_smile()}",
                                    reply_markup=main_keyboard())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!",
                                    reply_markup=main_keyboard())


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text,
                                    reply_markup=main_keyboard())
    

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    file_id = update.message.photo[-1].file_id
    new_file = await context.bot.get_file(file_id)
    
    await new_file.download_to_drive()
    await update.message.reply_text(f'Изображение получено!\n Наложение фильтра в процессе....')