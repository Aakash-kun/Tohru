from nextcord import Intents, AllowedMentions
from nextcord.ext import commands

import lavalink

from loguru import logger
from traceback import format_exc

from internal.guild import MyGuild
from internal.db import Database
from internal.player import CustomPlayer


class BotBase(commands.Bot):
    """ Custom Bot Class to add more functionalities """
    
    def __init__(self, *args, **kwargs):

        logger.info("Starting up the bot's engine...")

        intents = Intents.all()
        super().__init__(command_prefix='.',
                         # ------------------ TODO: Will make a better Help cmd and add here...
                         help_command=None,
                         intents=intents,
                         allowed_mentions=AllowedMentions(
                             roles=False, 
                             everyone=False, 
                             users=False
                             ),
                         *args,
                         **kwargs)
        
        # helps to add persistent views
        self.persistent_views_added = False

        # so here when we get/fetch the guild,
        # it will return us our Custom Guild class.
        # Made by Skelmis (https://github.com/Skelmis)
        # Lob you Skelmis, Thank youuuuu
        self._old_get_guild = self.get_guild
        self._old_fetch_guild = self.fetch_guild

        self.get_guild = self.get_wrapped_guild
        self.fetch_guild = self.fetch_wrapped_guild

        # initiating the database
        # self.db = Database()  
        # TODO: Will make a better database class later
        
    def get_wrapped_guild(self, guild_id):
        """ Returns the guild with the given ID. """
        guild = self._old_get_guild(guild_id)
        return MyGuild(guild, bot=self)

    async def fetch_wrapped_guild(self, guild_id):
        """ Returns the guild with the given ID. """
        guild = await self._old_fetch_guild(guild_id)
        return MyGuild(guild, bot=self)

    def add_cog(self, cog):
        logger.info(f"Loading cog {cog.qualified_name}...")
        return super().add_cog(cog)

    def load_extensions(self, *exts):
        """ Loads a list of extensions. """
        for ext in exts:
            try:
                self.load_extension(ext)
            except Exception as e:
                logger.error(
                    f"Error while loading {ext}: {e}:\n{format_exc()}")
            else:
                logger.info(f"Successfully loaded extension {ext}.")

    async def on_ready(self):
        """ Connects to the Lavalink server and logs the info."""
        self.lavalink: lavalink.Client = lavalink.Client(self.user.id, player=CustomPlayer)
        self.lavalink.add_node(
            '127.0.0.1', 2333, 'youshallnotpass', 'india', 'default-node')
        logger.info("Connected to Lavalink.")
        logger.info("Bot is ready to bash.")
