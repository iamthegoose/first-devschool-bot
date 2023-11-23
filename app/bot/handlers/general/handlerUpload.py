from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from app.utils.fileUpload import Upload
from app.messages.uploadmessages import FILENAME_MSG, FILEUPLOAD_MSG, FILEACCEPTED_MSG


async def upload(message: Message, state: FSMContext) -> None:
    # if message.text == '/upload' or message.text.lower() == 'upload the file':
    await message.answer(
        await FILENAME_MSG.render_async(name=message.from_user.first_name)# type: ignore[union-attr]
    )
    await state.set_state(Upload.filename)


async def upload_file(message: Message, state: FSMContext) -> None:
    await state.update_data(filename=message.text)

    await message.answer(
        await FILEUPLOAD_MSG.render_async()
    )
    await state.set_state(Upload.file)


async def file_accepted(message: Message, state: FSMContext, bot: Bot) -> None:
    if message.document:
        document_id = message.document.file_id
        file_name = message.document.file_name
        extension = file_name[file_name.index(".")+1::]# type: ignore[union-attr, index]
        file_info = await bot.get_file(document_id)
        file_path = file_info.file_path
        data = await state.get_data()
        file_destination = f"files/{data['filename']}.{extension}"# type: ignore[name-defined]
        await bot.download_file(file_path, file_destination)# type: ignore[arg-type]
        await message.answer(
            await FILEACCEPTED_MSG.render_async()
        )
        await state.clear()
    else:
        await message.answer("This file is not supportable. Remove check on 'compress the image'")
