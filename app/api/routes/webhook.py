from aiogram import Bot, Dispatcher
from aiogram.types import Update
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.api.stubs import BotStub, DispatcherStub

webHookRouter = APIRouter(prefix = "/webhook", tags = ["Telegram Webhook"])

@webHookRouter.post("")
async def webHookRoute(
        update: Update,
        bot: Bot = Depends(BotStub),
        dispatcher: Dispatcher = Depends(DispatcherStub),
    ) -> JSONResponse:
    await dispatcher.feed_update(bot, update=update)
    return JSONResponse(status_code=200, content={"ok": True})
