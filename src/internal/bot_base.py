from typing import Union
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from nextcord import Guild, Member, User
from nextcord.ext import commands

class BotBaseBot(commands.Bot):
	async def getch_guild(self, guild_id: int) -> Union[Guild, bool]:
		"""Looks up a guild in cache or fetches if not found."""
		guild: Union[Guild, None] = self.get_guild(guild_id)
		if guild:
			return guild

		try:
			guild: Union[Guild, None] = await self.fetch_guild(guild_id)
		except:
			return False
		return guild

	async def getch_user(self, user_id: int) -> Union[User, bool]:
		"""Looks up a user in cache or fetches if not found."""
		user: Union[User, None] = self.get_user(user_id)
		if user:
			return user
		try:
			user: Union[User, None] = await self.fetch_user(user_id)
		except:
			return False
		return user

	async def getch_member(self, guild_id: int, member_id: int) -> Union[Member, bool]:
		"""Looks up a member in cache or fetches if not found."""

		guild: Union[Member, None] = await self.getch_guild(guild_id)
		if not guild:
			return False

		member: Union[Member, None] = guild.get_member(member_id)
		if member is not None:
			return member

		try:
			member: Union[Member, None] = await guild.fetch_member(member_id)
		except:
			return False

		return member

	async def getch_channel(self, channel_id: int) -> Union[GuildChannel, bool]:
		"""Looks up a channel in cache or fetches if not found."""
		channel: Union[GuildChannel, None] = self.get_channel(channel_id)
		if channel:
			return channel

		try:
			channel: Union[GuildChannel, None] = await self.fetch_channel(channel_id)
		except:
			return False

		return channel

	async def resync_slash_commands(self) -> None:
		for app_cmd in self.get_all_application_commands():
			if not app_cmd.command_ids:
				if app_cmd.is_guild:
					for guild_id in app_cmd.guild_ids_to_rollout:
						guild = self.get_guild(guild_id)
						await guild.rollout_application_commands()
