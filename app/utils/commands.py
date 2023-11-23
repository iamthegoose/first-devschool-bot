from aiogram.types import BotCommand
from aiogram import Bot
from typing import List


async def set_bot_commands(bot: Bot) -> None:
    commands: List[BotCommand] = [
        BotCommand(command="start", description="starting command"),
        BotCommand(command="upload", description="uploading a file"),
        BotCommand(command="download", description="uploading a file"),
        BotCommand(command="fromlink", description="uploading a file")
    ]
    await bot.set_my_commands(commands=commands)
