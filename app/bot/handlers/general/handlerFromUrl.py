import validators
import requests

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, URLInputFile
from app.utils.states.linkDownload import LinkState


async def fromurl(message: Message, state: FSMContext):
    await state.set_state(LinkState.sending_url)
    await message.answer("<i><b>Please send your url</b></i>")


async def send_file(message: Message, state: FSMContext):

    if not validators.url(message.text):
        await message.answer("<ins>Invalid URL!</ins>")
        return

    url = message.text

    response = requests.head(url)

    if 'image' not in response.headers.get('content-type', '').lower():
        await message.answer("<b>There is no image in the URL\!</b>")
        return

    urlimage = URLInputFile(url)

    await message.answer_photo(urlimage)
    await state.clear()
