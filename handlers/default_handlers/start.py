from bot import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def hullo(message: Message) -> None:
    """A func for sending some good ol' 'Hullo'! """

    await message.reply("<i>Hullo</i>!")


@dp.message_handler(commands="dice")
async def cmd_dice(message: Message):
    await message.answer_dice()
