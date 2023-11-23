from aiogram.types import Message
# from app.messages.start_message import START
from app.messages.uploadmessages import FILENAME_MSG
from app.bot.keyboard.downloadkb import download_Keyboard


async def inline(message: Message):
    await message.answer(
        await FILENAME_MSG.render_async(name=message.from_user.first_name),# type: ignore[union-attr]
        reply_markup=await download_Keyboard()
    )
