from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
import os
from glob import glob


def get_smile():
    smile = emojize("😃")
    return smile


def main_keyboard():
    return ReplyKeyboardMarkup([['Возможности', 'Отправить изображение']])


def precessing_image():
    os.makedirs('downloads/after_processing', exist_ok=True)

    file_list = glob('downloads/before_processing/*_orig.****')
    print(file_list)


if __name__ == "__main__":
    precessing_image()