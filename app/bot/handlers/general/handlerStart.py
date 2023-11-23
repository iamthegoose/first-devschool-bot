from aiogram.types import Message
from app.messages.start_message import START
from app.bot.keyboard.kb import keyboardBuild


async def start(message: Message) -> None:

    await message.answer(await START.render_async(name=message.from_user.first_name), reply_markup=await keyboardBuild())# type: ignore[union-attr]
