from aiogram import types


def what_group_kb() -> types.InlineKeyboardMarkup:
    """
    Func that returns a keyboard from what you can choose which group's song you want to random
    """
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button_eli = types.InlineKeyboardButton(text='Елизаров', callback_data='eli')
    button_ramm = types.InlineKeyboardButton(text='Rammstein', callback_data='ramm')
    button_site = types.InlineKeyboardButton(text='Gonna go with the site',
                                             url='https://mydeartestingground.000webhostapp.com/')

    keyboard.add(button_eli, button_ramm, button_site)

    return keyboard


def eli_menu() -> types.InlineKeyboardMarkup:
    """Returns a keyboard for elizarov-randomizing"""

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="🌀 - every song", callback_data="eb_blue_button"),
        types.InlineKeyboardButton(text="♨️ - the least", callback_data="eb_red_button"),
        types.InlineKeyboardButton(text="🟢 - purified ", callback_data="eb_green_button"),
        types.InlineKeyboardButton(text="✴️ - good ones", callback_data="eb_orange_button"),
        types.InlineKeyboardButton(text="✡️ - the best ", callback_data="eb_violet_button"),
        types.InlineKeyboardButton(text="🎟️ - covers", callback_data="eb_pink_button"),
        types.InlineKeyboardButton(text="💀", callback_data="eb_black_button")
        ]

    keyboard.add(*buttons)

    return keyboard


def ramm_menu() -> types.InlineKeyboardMarkup:
    """Returns a keyboard for rammstein-randomizing"""

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="🔷 - every song", callback_data="rb_blue_button"),
        types.InlineKeyboardButton(text="🩸️ - the least", callback_data="rb_red_button"),
        types.InlineKeyboardButton(text="🟢 - purified ", callback_data="rb_green_button"),
        types.InlineKeyboardButton(text="🚼️ - good ones", callback_data="rb_orange_button"),
        types.InlineKeyboardButton(text="🚺️ - the best ", callback_data="rb_violet_button"),
        types.InlineKeyboardButton(text="👯‍♂️ - covers", callback_data="rb_pink_button"),
        types.InlineKeyboardButton(text="👻", callback_data="rb_black_button")
    ]

    keyboard.add(*buttons)

    return keyboard


def go_to_menu(youtube_song_name: str, yandex_song_name: str) -> types.InlineKeyboardMarkup:
    """returns a keyboard with to url's buttons - to go to YouTube and Yandex.Music"""

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text="YouTube", url=f"https://www.youtube.com/results?search_query={youtube_song_name}"),
        types.InlineKeyboardButton(text="Yandex.Music", url=f"https://music.yandex.ru/search?text={yandex_song_name}")
    ]

    keyboard.add(*buttons)

    return keyboard
