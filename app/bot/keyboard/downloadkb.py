from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os


async def download_Keyboard():
    path = r'files/'
    files = os.listdir(path)
    builder = InlineKeyboardBuilder()
    for filename in files:
        if os.path.isfile(os.path.join(path, filename)):
            builder.row(InlineKeyboardButton(
                text=filename,
                callback_data=filename,
                file = filename
            ), width=1)
    return builder.as_markup()
