from bot import dp
from aiogram.types import Message


@dp.message_handler(content_types=['photo'])
async def download_photo(message: Message) -> None:
    await message.photo[-1].download(destination_dir=r'C:\Me\Coding_server')
    await message.answer(text='The photo has been downloaded!')
