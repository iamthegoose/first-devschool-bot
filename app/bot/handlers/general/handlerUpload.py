from aiogram.types import Message 
from aiogram import Bot
import aiofiles
from aiohttp import ClientSession
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
    global filename
    filename = message.text
    await message.answer(
        await FILEUPLOAD_MSG.render_async()
    )
    await state.set_state(Upload.file)


async def file_accepted(message:Message, state:FSMContext, bot:Bot) -> None:
    if message.document:
    # Отримання інформації про файл
        file_info = await bot.get_file(message.document.file_id)
        # Отримання прямого посилання на файл
        file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"
        async with ClientSession() as session:  
            async with session.get(file_url) as response:
                
                async with aiofiles.open(f"D:/bots/bot-dev-1/files/{filename}.txt", "x") as file:
                    await file.write(await response.text())
        await message.answer(
            await FILENAME_MSG.render_async(name = message.from_user.first_name)
        )
        await state.clear()
    else:
        await message.answer("bruh bruh bruh")


# async def upload_file(message:Message, bot:Bot):
#     # Перевірка, чи повідомлення містить файл
#     if message.document:
#         # Отримання інформації про файл
#         file_info = await bot.get_file(message.document.file_id)
#         # Отримання прямого посилання на файл
#         file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"
#         async with ClientSession() as session:
#             async with session.get(file_url) as response:
#                 async with open("../../../../../files", "wb") as file:
#                     file.write(response.content)

#         # response = requests.get(file_url)
        # with open("downloaded_file.txt", "wb") as file:
        #     file.write(response.content)
        # #     print("Файл було завантажено")