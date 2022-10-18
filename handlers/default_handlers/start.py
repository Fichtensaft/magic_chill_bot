from bot import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def hullo(message: Message) -> None:
    """A func for sending some good ol' 'Hullo'! """

    await message.answer("<b><i>Hello!</i></b>\nType /menu to really start!")


@dp.message_handler(commands="dice")
async def cmd_dice(message: Message):
    await message.answer_dice()
