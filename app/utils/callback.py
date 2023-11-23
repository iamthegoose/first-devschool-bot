from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile, Message
# from app.bot.handlers.general.handlerDownload import download


async def de_inline(cb: CallbackQuery, bot: Bot):
    filename = cb.data
    file_path = f'files/{filename}'
    file = FSInputFile(file_path)
    await cb.message.answer_document(file)
    await cb.answer()
