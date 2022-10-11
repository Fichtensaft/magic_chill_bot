from bot import dp
from aiogram.types import Message


@dp.message_handler(commands=['hello'])
async def hullo(message: Message) -> None:
    """A func for sending some good ol' 'Hullo'! """

    await message.reply("Hullo!")
