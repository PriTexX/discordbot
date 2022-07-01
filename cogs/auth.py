import discord
from discord.ext import commands
from utils.user import UserAuth, getUser
from guild import RoleManager, UserManager
from exceptions import FailedToLoginException
from discord_components import Interaction
from components import EventHandler


class Auth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.on_button_press.registerHandler("auth_button", EventHandler("auth", self.auth_handler, self.bot))

    @staticmethod
    async def auth_handler(bot, interaction):
        await interaction.respond(type=6)

        await interaction.author.send("Напишите мне в ответ свои логин и пароль от лк")
        response = await bot.wait_for("message",
                                      timeout=60,
                                      check=lambda x: x.author.id == interaction.author.id
                                      )
        try:
            login, password = response.content.split()
        except ValueError:
            await interaction.author.send("Неверный логин или пароль")
            return

        await Auth.auth(interaction.author, interaction.guild, login, password)

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
        await self.bot.on_button_press.handle(interaction.custom_id, interaction)
        f = self.bot.cogs[0]
        print(f)


def setup(bot):
    bot.add_cog(Auth(bot))