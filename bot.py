import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

from config_data.config import BOT_TOKEN


# Initialize logging
logging.basicConfig(level=logging.INFO, filename='mc_log.log', filemode='w')

# Initialize bot and dispatcher

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

# creating a new branch