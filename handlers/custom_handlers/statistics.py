from bot import dp
from aiogram import types
from keyboards.ReplyKeyboards import statistics_replyes
from keyboards.inline_keyboards import statistics_inlines
from keyboards.inline_keyboards import random_songs_inlines
from aiogram.dispatcher.filters import Text
# from database.master_db import da_base, cur

import sqlite3
import asyncio

da_base = sqlite3.connect(r'C:\Me\Coding_Python\Projects\Magic_Chill\database\songs.db', check_same_thread=False)
cur = da_base.cursor()


@dp.message_handler(lambda message: message.text == 'Statistics 📊')
async def stat_menu(message: types.Message) -> None:
    await message.answer(text="Let's see statistics!", reply_markup=statistics_replyes.stat_menu())


@dp.message_handler(lambda message: message.text == 'Songs 🎶')
async def stat_menu(message: types.Message) -> None:
    await message.answer(text="Which group's statistics?", reply_markup=statistics_inlines.groups_menu())


@dp.callback_query_handler(text='eli_tab')
async def eli_stats(call: types.CallbackQuery):
    ...
