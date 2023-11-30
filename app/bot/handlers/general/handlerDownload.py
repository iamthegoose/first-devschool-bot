from aiogram.types import Message
from app.messages.downloadmessages import DOWNLOAD_MSG
from app.bot.keyboard.downloadkb import download_Keyboard


async def inline(message: Message):
    await message.answer(
        await DOWNLOAD_MSG.render_async(),  # type: ignore[union-attr]
        reply_markup=await download_Keyboard()
    )
