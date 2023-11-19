from aiogram import Router
from aiogram.filters import CommandStart, Command
from app.utils.fileUpload import Upload

from app.bot.handlers.general.handlerStart import start
# from app.bot.handlers.general.handlerHelp import help
from app.bot.handlers.general.handlerUpload import upload, upload_file, file_accepted

router = Router(name = __name__)

router.message.register(start, CommandStart())
# router.message.register(help, Command("help"))
router.message.register(upload, Command("upload"))
router.message.register(upload_file, Upload.filename)
router.message.register(file_accepted, Upload.file)