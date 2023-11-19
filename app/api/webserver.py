from typing import Any

from aiogram import Bot, Dispatcher
from fastapi import FastAPI
from pydantic import AnyUrl
from app.api.stubs import *
from app.api.routes.webhook import webHookRouter
from app.settings import settings


def create_app(bot: Bot, dp: Dispatcher) -> FastAPI:
    app = FastAPI()

    app.include_router(webHookRouter)

    workflow_data = {
        "app": app,
        "dp": dp,
        "bot": bot,
        **dp.workflow_data,
    }
    app.dependency_overrides.update(
        {
            BotStub: lambda: bot,
            DispatcherStub: lambda: dp,
        }
    )

    async def on_startup(*args: Any, **kwargs: Any) -> None:  # pragma: no cover
        if settings.DEVELOPMENT:
            from ngrok import ngrok
            tunnel = await ngrok.connect(8000)  # type: ignore[misc]
            public_url = tunnel.url()
            settings.BASE_URL = AnyUrl(public_url)
        await dp.emit_startup(**workflow_data)

    async def on_shutdown(*args: Any, **kwargs: Any) -> None:  # pragma: no cover
        if settings.DEVELOPMENT:
            from ngrok import ngrok
            ngrok.disconnect()
        await dp.emit_shutdown(**workflow_data)

    app.add_event_handler('startup', on_startup)
    app.add_event_handler('shutdown', on_shutdown)

    return app