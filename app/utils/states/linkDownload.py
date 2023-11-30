from aiogram.fsm.state import StatesGroup, State


class LinkState(StatesGroup):
    sending_url = State()