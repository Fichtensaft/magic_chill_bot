from bot import dp
from aiogram.types import Message
from aiogram import types


def main_menu_kb() -> types.ReplyKeyboardMarkup:
    main_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,row_width=2)
    buttons = [
        types.KeyboardButton(text="Let's random 🎲"),
        types.KeyboardButton(text="Memorize 🧠!"),
        types.KeyboardButton(text="Statistics 📊")
        ]
    main_kb.add(*buttons)

    return main_kb
