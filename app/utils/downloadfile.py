from app import bot

async def downloadFile(file, destination) -> None:
    await bot.download(file, destination)