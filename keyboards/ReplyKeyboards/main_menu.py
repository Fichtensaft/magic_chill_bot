from bot import dp
from aiogram.types import Message
from aiogram import types


def main_menu_kb() -> types.ReplyKeyboardMarkup:
    main_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = types.KeyboardButton(text="Let's random 🎲")
    button_2 = types.KeyboardButton(text="Memorize 🧠!")
    main_kb.add(button_1, button_2)

    return main_kb
