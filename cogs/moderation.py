import discord
from discord.ext import commands
from utils.user import UserAuth, getUser
from guild import RoleManager, UserManager
from exceptions import FailedToLoginException


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount=1):
        if amount < 1: amount = 1

        await ctx.channel.purge(limit=amount + 1)


def setup(bot):
    bot.add_cog(Moderation(bot))
