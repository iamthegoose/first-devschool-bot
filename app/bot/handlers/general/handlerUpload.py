from aiogram.types import Message
# from app.messages.start_message import START
from aiogram.fsm.context import FSMContext
from app.utils.fileUpload import Upload
from app.utils.downloadfile import downloadFile
from app.messages.uploadmessages import FILENAME_MSG, FILEUPLOAD_MSG, FILEACCEPTED_MSG


async def upload(message:Message, state:FSMContext) -> None:
    await message.answer(
        await FILENAME_MSG.render_async(name = message.from_user.first_name)
    )
    await state.set_state(Upload.filename)
    


async def upload_file(message:Message, state:FSMContext) -> None:
    await state.update_data(filename = message.text)
    await message.answer(
        await FILEUPLOAD_MSG.render_async()
    )
    await state.set_state(Upload.file)
    file = message.document
    await downloadFile(file = file, destination="../files")
    await message.answer(
        await FILEACCEPTED_MSG.render_async(destination = "../files")
    )


async def file_accepted(message:Message, state:FSMContext) -> None:
    await message.answer(
        await FILENAME_MSG.render_async(name = message.from_user.first_name)
    )
    await state.clear()