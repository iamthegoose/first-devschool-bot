from aiogram import types


async def keyboardBuild():
    kb = [
        [
            types.KeyboardButton(text="Upload the file"),
            types.KeyboardButton(text="Download the file"),
            types.KeyboardButton(text="Download the file from the link")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Choose what you would like to do"
    )
    return keyboard
