from aiogram.types import Message
from app.messages.start_message import START
async def start(message:Message) -> None:
    await message.answer(START)