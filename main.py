from internal.bot import BotBase
from config import token

bot = BotBase()

bot.load_extensions('jishaku',
                    'cogs.music_commands')

bot.run(token)
