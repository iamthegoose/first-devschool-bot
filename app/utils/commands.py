from aiogram.types import BotCommand
from aiogram import Bot
from typing import List


async def set_bot_commands(bot: Bot) -> None:
    commands: List[BotCommand] = [
        BotCommand(command="start", description="starting command"),
        BotCommand(command="upload", description="upload a file"),
        BotCommand(command="download", description="download a file"),
        BotCommand(command="fromlink", description="download the file from the link")
    ]
    await bot.set_my_commands(commands=commands)
