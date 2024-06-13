import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from bot.handlers import dp
from bot.dispatcher import TOKEN
from db.config import engine
from db.models import Base
from utils.middlewares import CustomMiddleware

def on_startup():
    Base.metadata.create_all(engine)

async def register_all_middleware():
    dp.update.middleware(CustomMiddleware())
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await register_all_middleware()
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())