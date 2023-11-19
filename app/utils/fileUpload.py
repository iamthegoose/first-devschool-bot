from aiogram.fsm.state import State, StatesGroup

class Upload(StatesGroup):
    filename = State()
    file = State()
    