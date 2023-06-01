from telegram import Update
from telegram.ext import ContextTypes
from utils import get_smile, main_keyboard, precessing_image
import os


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
    

async def get_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Обрабатываем изображение')
    # user_message_id = update.message.message_id
    photo_file_id = update.message.photo[-1].file_id
    received_image = await context.bot.get_file(photo_file_id)
    os.makedirs('downloads/before_processing', exist_ok=True)
    file_name = os.path.join('downloads', 'before_processing', f'{photo_file_id}_orig.jpg')
    await received_image.download_to_drive(file_name)
    await update.message.reply_text('Изображение сохранено')
    await update.message.reply_text('Наложение фильтра в процессе....')


async def send_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass