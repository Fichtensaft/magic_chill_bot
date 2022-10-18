from bot import dp
from aiogram import types
from keyboards.inline_keyboards import random_songs_inlines
from aiogram.dispatcher.filters import Text
# from database.master_db import da_base, cur

import sqlite3

da_base = sqlite3.connect(r'C:\Me\Coding_Python\Projects\Magic_Chill\database\songs.db', check_same_thread=False)
cur = da_base.cursor()


def sql_song_req(tab_name: str, but_colour: str) -> str:
    """Function to make a proper sql-request"""

    return "SELECT a_song FROM {t_name} WHERE {but_col}=1 ORDER BY RANDOM() LIMIT 1".format(t_name=tab_name,
                                                                                            but_col=but_colour)


def youtube_search(song_name: str, group_name: str) -> str:
    """
    Function to make a proper YouTube URL
    """

    name_with_pluses = '+'.join(song_name.split())
    dash_split_name = name_with_pluses.split('+-+')
    dash_split_name[0] = group_name

    return '+'.join(dash_split_name)


def yandex_search(song_name: str) -> str:
    """Function to make a 'proper' (at least working ;)) yandex-music request - URL"""

    split_song = song_name.split()
    split_song.remove('-')

    return ''.join(split_song)


@dp.message_handler(lambda message: message.text == "Let's random 🎲")
async def random_song_start(message: types.Message) -> None:
    """Calling for keyboard to the 'command' from main menu"""

    await message.answer(f"Which group?", reply_markup=random_songs_inlines.what_group_kb())


# Elizarov Part
@dp.callback_query_handler(text='eli')
async def random_eli_start(call: types.CallbackQuery) -> None:
    """Sending a keyboard to user for elizarov randomizing"""

    await call.message.answer(text='Choose a button!', reply_markup=random_songs_inlines.eli_menu())


@dp.callback_query_handler(Text(startswith="eb_"))
async def random_eli_pick(call: types.CallbackQuery) -> None:
    """Choosing the button to randomize a elizarov-song at last"""

    tab_name = 'eli_songs'
    button_colour = call.data[3:]
    sql_req = sql_song_req(tab_name=tab_name, but_colour=button_colour)

    random_song_exec = cur.execute(sql_req)
    randomized_song = random_song_exec.fetchall()[0][0]

    await call.message.answer(text=randomized_song,
                              reply_markup=random_songs_inlines.go_to_menu(
                                  youtube_song_name=youtube_search(randomized_song, "Елизаров"),
                                  yandex_song_name=yandex_search(randomized_song))
                              )
    await call.answer()


# Rammstein Part
@dp.callback_query_handler(text='ramm')
async def random_ramm_start(call: types.CallbackQuery) -> None:
    """Sending a keyboard to user for rammstein randomizing"""

    await call.message.answer(text='Choose a button!', reply_markup=random_songs_inlines.ramm_menu())


@dp.callback_query_handler(Text(startswith="rb_"))
async def random_ramm_pick(call: types.CallbackQuery) -> None:
    """Choosing the button to randomize a rammstein-song at last"""

    tab_name = 'ramm_songs'
    button_colour = call.data[3:]
    sql_req = sql_song_req(tab_name=tab_name, but_colour=button_colour)

    random_song_exec = cur.execute(sql_req)
    randomized_song = random_song_exec.fetchall()[0][0]

    await call.message.answer(text=randomized_song,
                              reply_markup=random_songs_inlines.go_to_menu(
                                  youtube_song_name=youtube_search(randomized_song, "Rammstein"),
                                  yandex_song_name=yandex_search(randomized_song)
                              ))
    await call.answer()
