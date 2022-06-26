import discord
from discord.ext import commands
from utils.user import UserAuth, getUser
from guild import RoleManager, UserManager
from exceptions import FailedToLoginException


class Auth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def auth(self, ctx, login, password):
        try:
            userToken = UserAuth.auth(login, password)
        except FailedToLoginException:
            await ctx.send(f"Неверный логин или пароль")
            return

        user = getUser(userToken)
        role = RoleManager.getRole(ctx.guild, user.group)

        if not role:
            role = await RoleManager.createRole(ctx.guild, user.group)

        await UserManager.addRoles(ctx.author, role, reason="Added by bot, adding new user role")
        await UserManager.changeNickname(ctx.author, nick=user.name, reason="Changed by bot, authenticating new user")


def setup(bot):
    bot.add_cog(Auth(bot))