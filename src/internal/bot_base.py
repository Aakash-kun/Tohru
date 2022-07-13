from typing import Optional, Union
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from nextcord import Guild, Member, User
from nextcord.ext import commands

class BotBase(commands.Bot):
	async def get_or_fetch_guild(self, guild_id: int) -> Optional[Guild]:
		"""Looks up a guild in cache or fetches if not found."""
		guild: Optional[Guild] = self.get_guild(guild_id)
		if guild:
			return guild

		try:
			guild: Guild = await self.fetch_guild(guild_id)
		except:
			return False

		return guild

	async def get_or_fetch_user(self, user_id: int) -> Optional[User]:
		"""Looks up a user in cache or fetches if not found."""
		user: Optional[User] = self.get_user(user_id)
		if user:
			return user
		try:
			user: User = await self.fetch_user(user_id)
		except:
			return False

		return user

	async def get_or_fetch_member(self, guild_id: int, member_id: int) -> Optional[Member]:
		"""Looks up a member in cache or fetches if not found."""

		guild: Optional[Guild] = await self.get_or_fetch_guild(guild_id)
		if not guild:
			return False

		member: Optional[Member] = guild.get_member(member_id)
		if member is not None:
			return member

		try:
			member: Member = await guild.fetch_member(member_id)
		except:
			return False

		return member

	async def get_or_fetch_channel(self, channel_id: int):
		"""Looks up a channel in cache or fetches if not found."""
		channel = self.get_channel(channel_id)
		if channel:
			return channel

		try:
			channel = await self.fetch_channel(channel_id)
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
