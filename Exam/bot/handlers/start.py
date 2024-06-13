from aiogram import html, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.utils.i18n import gettext as _
from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from bot.buttons.reply import main_button, menu_button
from db.models import User
main_router = Router()


class Menues(StatesGroup):
    main_menu = State()
    back1 = State()

@main_router.message(CommandStart())
async def command_start_handler(message: Message, session: Session, state: FSMContext) -> None:
    is_exists = session.execute(select(User).where(User.user_id == message.from_user.id)).scalar()
    if not is_exists:
        user = {
            "user_id": message.from_user.id,
            "username": message.from_user.username,
            "full_name": message.from_user.full_name
        }
        session.execute(insert(User).values(**user))
        session.commit()
        await state.set_state(Menues.main_menu)
    await message.answer_photo(photo='https://telegra.ph/file/f66796c4441795e4b38f5.png', caption="""Assalomu alaykum ! 
    Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi""", reply_markup=await main_button())

@main_router.message(F.text == "Filial 📍")
async def filial_handler(message: Message) -> None:
    await message.answer_location(longitude=69.253043, latitude=41.304476)



@main_router.message(F.text == "Admin 👨🏻‍💻")
async def admin_handler(message: Message) -> None:
    link = "https://t.me/Asilbek072103"
    await message.answer(link)

@main_router.message(F.text=="Start ✅")
async def menu_handler(message: Message, state: FSMContext):
    await state.set_state(Menues.back1)
    await message.answer(text='Quydagilardan birontasini tanlang 👇', reply_markup= await menu_button())





@main_router.message(F.text == "🔙 back")
async def back_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state == Menues.back1.state:
        await command_start_handler(message, state)


