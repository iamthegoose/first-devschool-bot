# from aiogram import Router, F
# from app.bot.keyboard.downloadkb import markup
# from aiogram.filters import Filter

# router = Router(name=__name__)
# regexp = r'\\d+'
# for button_index in range(len(markup.inline_keyboard)):
#     router.callback_query.register(get_id, F.foo == f'download{button_index}')

# router.message.register(download, F.text==f"Download {markup.inline_keyboard[int(regexp)]}")