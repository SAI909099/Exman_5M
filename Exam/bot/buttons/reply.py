from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def main_button():
    rkm = ReplyKeyboardBuilder()
    rkm.add(*[KeyboardButton(text="Filial 📍"), KeyboardButton(text="Start ✅"),
              KeyboardButton(text="Admin 👨🏻‍💻")])
    rkm.adjust(2, 1)
    rkm = rkm.as_markup(resize_keyboard=True)
    return rkm


async def menu_button():
    rkm = ReplyKeyboardBuilder()
    rkm.add(*[KeyboardButton(text="Woman 🧍‍♀️"), KeyboardButton(text="Men 🧍‍♂️"),
              KeyboardButton(text="🔙 back")])
    rkm.adjust(2, 1)
    rkm = rkm.as_markup(resize_keyboard=True)
    return rkm