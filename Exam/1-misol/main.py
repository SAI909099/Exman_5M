import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import MemoryStorage
from aiogram.utils import executor
import aiosmtplib
from email.mime.text import MIMEText

API_TOKEN = '7141006466:AAECZwyH6pvMZfmhk5xYsq5g4UH7igf38Uc'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
EMAIL_USER = 'sizning emailingiz @gmail.com'
EMAIL_PASSWORD = 'your_password'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


class Form(StatesGroup):
    email = State()
    message = State()


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await Form.email.set()
    await message.reply("Assalomu alaykum! Menga elektron pochta manzilingizni kiriting:")


@dp.message_handler(state=Form.email)
async def process_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await Form.next()
    await message.reply("Rahmat! Endi, yuboriladigan xabarni kiriting:")


@dp.message_handler(state=Form.message)
async def process_message(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    email = user_data['email']
    message_text = message.text

    await send_email(email, message_text)

    await message.reply("Xabar muvaffaqiyatli yuborildi!")
    await state.finish()


async def send_email(email, message_text):
    msg = MIMEText(message_text)
    msg['Subject'] = 'Telegram Bot Xabari'
    msg['From'] = EMAIL_USER
    msg['To'] = email

    async with aiosmtplib.SMTP(hostname=SMTP_SERVER, port=SMTP_PORT, use_tls=True) as server:
        await server.login(EMAIL_USER, EMAIL_PASSWORD)
        await server.send_message(msg)


@dp.message_handler(commands='cancel', state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply('Amal bekor qilindi.', reply=False)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
