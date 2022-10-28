from aiogram import types


def stat_menu() -> types.ReplyKeyboardMarkup:
    stat_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    buttons = [
        types.KeyboardButton(text="Songs 🎶"),
        types.KeyboardButton(text="Parties 🥳")
    ]
    stat_kb.add(*buttons)

    return stat_kb
