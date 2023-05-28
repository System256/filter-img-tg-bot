from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_smile():
    smile = emojize("😃")
    return smile


def main_keyboard():
    return ReplyKeyboardMarkup([['/help', 'Тест']])