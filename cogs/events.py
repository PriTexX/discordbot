import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('...'))
        DiscordComponents(self.bot)
        print("Ready")


def setup(bot):
    bot.add_cog(Event(bot))
