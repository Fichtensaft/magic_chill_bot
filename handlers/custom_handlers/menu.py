from bot import dp
from aiogram.types import Message
from aiogram import types
from keyboards.ReplyKeyboards.main_menu import main_menu_kb


@dp.message_handler(commands=['menu'])
async def cmd_main_menu(message: Message) -> None:
    await message.answer('What are we gonna do?', reply_markup=main_menu_kb())
