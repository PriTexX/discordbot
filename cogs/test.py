import discord
from discord.ext import commands
from utils.user import UserAuth, getUser
from guild import RoleManager, UserManager
from exceptions import FailedToLoginException
from discord_components import ButtonStyle, Button, Interaction


class Test(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.author.send("Reply on this msg")

        msg = await self.bot.wait_for("message")
        await ctx.send(msg.content)

    @commands.command()
    async def test2(self, ctx):
        await ctx.send(
            embed=discord.Embed(title="Авторизация"),
            components=[
                Button(style=ButtonStyle.green, label="Авторизоваться", custom_id="auth_button"),
            ]
        )


def setup(bot):
    bot.add_cog(Test(bot))
