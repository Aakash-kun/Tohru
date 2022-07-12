from bot_base import BotBaseBot
from nextcord import Intents
from config_handler import Config
import aiosqlite

bot: BotBaseBot = BotBaseBot(command_prefix=".", intents=Intents.all(), strip_after_prefix=True)

cogs: list[str] = [
    "jishaku",
    "cogs.owners"

    "cogs.music_commands",
    "cogs.music_events",
    "cogs.ui"
]

@bot.event
async def on_ready() -> None:
	print(f"Logged in as {bot.user}")

async def startup():
	print("starting up...")
	bot.selfrole_view_set = False
	bot.support_view_set = False
	bot.owner_id = 707964352199786648

	await bot.wait_until_ready()

	# db stuff
	bot.db = await aiosqlite.connect(bot.config.get("db_file"))
	print("Setup DB")

	# cogs
	for extension in cogs:
		try:
			bot.load_extension(extension)
			print(f"Successfully loaded extension {extension}")
		except Exception as e:
			exc = f"{type(e).__name__,}: {e}"
			print(f"Failed to load extension {extension}\n{exc}")

	await bot.resync_slash_commands()

	print("Synced slash commands")
	print("All Ready")

bot.config = Config("configs/config.json")
bot.guild_config = Config("configs/guild_config.json")
bot.loop.create_task(startup())
bot.run(bot.config.get("token"))