from aiogram import types


def groups_menu() -> types.InlineKeyboardMarkup:
    groups_kb = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Елизаров", callback_data='eli_tab'),
        types.InlineKeyboardButton(text="Rammstein", callback_data='ramm_tab'),
        types.InlineKeyboardButton(text="Король и Шут", callback_data='kaj_tab')
    ]

    groups_kb.add(*buttons)

    return groups_kb
