import logging
from app.api.webserver import create_app
from app.bot.factory import create_bot, create_dp

    
bot = create_bot()
dp = create_dp()
app = create_app(bot, dp)
logging.basicConfig(level = "DEBUG")