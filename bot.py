import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.types import FSInputFile
from aiogram.filters.command import Command
from config_reader import config
from convert import converter


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /бот
@dp.message(Command("бот"))
async def cmd_start(message: types.Message):
    await message.answer("Подсказка: '/картинка порода кличка, телефон, где сбежала, приметы'")
# Загрузка фото - бот ловит любую фотографию, отправленную ему
@dp.message(F.photo)
async def cmd_foto(message: types.Message) -> None:
    await bot.download(message.photo[-1], destination='pict/pet.jpg')
    await message.answer(f'Фото обновлено! Используйте команду /алерт чтобы создать новое объявление')

# Основная команда "алерт"
@dp.message(Command("алерт"))
async def alert_cmd(message: types.Message, command: Command):
    if command.args is None:
        await message.answer("Вы не передали данные")
        return
    t = message.text
    converter(t)

    await message.answer_photo(FSInputFile('pict/textalert.jpg', 'rb'))
        
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())