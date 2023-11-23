from aiogram.types import Message, FSInputFile
from aiogram import Bot
# from app.messages.start_message import START
from aiogram import types
from app.utils.downloadfile import downloadFile
from app.messages.uploadmessages import FILENAME_MSG, FILEUPLOAD_MSG, FILEACCEPTED_MSG
from app.bot.keyboard.downloadkb import download_Keyboard


async def download(message: Message, bot: Bot, callback_data) -> None:
    file_path = f'files/{callback_data.file}'
    file = FSInputFile(file_path)
    await bot.send_document(message.from_user.id, file)


async def inline(message: Message):
    await message.answer(
        await FILENAME_MSG.render_async(name=message.from_user.first_name),
        reply_markup=await download_Keyboard()
    )
