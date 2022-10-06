from bot import dp
from aiogram.types import Message
from config_data.config import TUPLE_OF_COMMANDS


@dp.message_handler(commands=['start'])
async def hullo(message: Message) -> None:
    """A func for sending some good ol' 'Hullo'! """

    await message.reply("Hullo!")


@dp.message_handler(commands=['help'])
async def help_me(message: Message) -> None:
    """In needing of some help"""

    await message.answer(f'I can do: {TUPLE_OF_COMMANDS} ')