from aiogram.types import CallbackQuery, FSInputFile
# from app.bot.handlers.general.handlerDownload import download


async def download(cb: CallbackQuery):
    if cb is not None:
        filename = cb.data
        file_path = f'files/{filename}'
        file = FSInputFile(file_path)
        await cb.message.answer_document(file) # type: ignore[union-attr]
        await cb.answer()
