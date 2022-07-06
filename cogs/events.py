import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, Interaction


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('...'))
        DiscordComponents(self.bot)
        print("Ready")

    @commands.Cog.listener()
    async def on_button_click(self, interaction: Interaction):
        await self.bot.on_button_press.handle(interaction.custom_id, interaction)


def setup(bot):
    bot.add_cog(Event(bot))
