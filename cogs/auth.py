import discord
from discord.ext import commands
from utils.user import UserAuth, getUser
from guild import RoleManager, UserManager
from exceptions import FailedToLoginException
from discord_components import Interaction


class Auth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def auth(member, guild, login, password):
        try:
            userToken = UserAuth.auth(login, password)
        except FailedToLoginException:
            await member.send(f"Неверный логин или пароль")
            return

        user = getUser(userToken)
        role = RoleManager.getRole(guild, user.group)

        if not role:
            role = await RoleManager.createRole(guild, user.group)

        await UserManager.addRoles(member, role, reason="Added by bot, adding new user role")
        await UserManager.changeNickname(member, nick=user.name, reason="Changed by bot, authenticating new user")

    @commands.Cog.listener()
    async def on_button_click(self, interaction: Interaction):
        if interaction.custom_id != "auth_button":
            return
        await interaction.respond(type=6)

        await interaction.author.send("Напишите мне в ответ свои логин и пароль от лк")
        response = await self.bot.wait_for("message",
                                           timeout=60,
                                           check=lambda x: x.author.id == interaction.author.id
                                           )
        try:
            login, password = response.content.split()
        except ValueError:
            await interaction.author.send("Неверный логин или пароль")
            return

        await Auth.auth(interaction.author, interaction.guild, login, password)


def setup(bot):
    bot.add_cog(Auth(bot))