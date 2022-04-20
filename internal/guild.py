from nextcord import Guild


class MyGuild(Guild):
    def __init__(self, guild: Guild, bot):
        self.guild = guild
        self.bot = bot

    def __getattr__(self, item):
        return getattr(self.guild, item)

    def __instancecheck__(self, instance):
        return isinstance(instance, type(self.guild))

    def __subclasscheck__(self, subclass):
        return issubclass(subclass, self.guild)

    @property
    def is_configured(self):
        return self.bot.db.check_server(self.guild.id)

# Contributions: Thanks to Skelmis (https://github.com/Skelmis) for helping with this stuff.
