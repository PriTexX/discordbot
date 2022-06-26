import discord
from discord.ext import commands
from utils.user import getUser, UserAuth
from guild import RoleManager
from exceptions import FailedToLoginException


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx, login, password):
       return


def setup(bot):
    bot.add_cog(Test(bot))