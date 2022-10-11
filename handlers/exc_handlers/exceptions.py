from bot import dp
from aiogram.types import Message, Update
from aiogram.utils.exceptions import BotBlocked


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: Update, exception: BotBlocked):
    """
    Func for working with blocking bot from the user
    """
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД

    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True
