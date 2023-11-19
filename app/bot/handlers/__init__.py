from aiogram import Router
from aiogram.filters import CommandStart, Command

from app.bot.handlers.general.handlerStart import start
from app.bot.handlers.general.handlerHelp import help

router = Router(name = __name__)

router.message.register(start, CommandStart())
router.message.register(help, Command("help"))
