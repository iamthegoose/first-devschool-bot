from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from app.settings import settings
from app.bot.handlers import router as mainrouter
from aiogram.enums import ParseMode
from app.utils.commands import set_bot_commands


async def on_startup(bot: Bot, dp: Dispatcher) -> None:
    await bot.delete_webhook()
    await set_bot_commands(bot)
    await bot.set_webhook(
        settings.WEBHOOK_URL,
        drop_pending_updates=True,
        secret_token=settings.TELEGRAM_SECRET.get_secret_value(),
        allowed_updates=dp.resolve_used_update_types()
    )


async def on_shutdown(bot: Bot) -> None:
    await bot.delete_webhook(drop_pending_updates=True)


def create_dp() -> Dispatcher:
    dp = Dispatcher()
    dp.include_routers(mainrouter)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    return dp


def create_bot() -> Bot:
    return Bot(token=settings.TOKEN.get_secret_value(), parse_mode=ParseMode.HTML)
