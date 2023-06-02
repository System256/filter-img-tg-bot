from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
import os
from glob import glob
from PIL import Image, ImageFilter


def get_smile():
    smile = emojize("😃")
    return smile


def main_keyboard():
    return ReplyKeyboardMarkup([['Возможности', 'Отправить изображение']])


def processing_image():
    os.makedirs('downloads\\after_processing', exist_ok=True)
    before_img_list = glob('downloads\\before_processing\*_orig.****')
    file_img = Image.open(before_img_list[0])
    file_extension = before_img_list[0].split('.')[-1]
    blurred_img = file_img.filter(ImageFilter.BLUR)
    blurred_img.save(f'downloads\\after_processing\\new_file.{file_extension}') 
    print(file_extension)


if __name__ == "__main__":
    processing_image()