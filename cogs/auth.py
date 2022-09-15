from asyncio import futures
from discord.ext import commands
from utils.user import UserAuth
from exceptions import UserAlreadyExists
from components import EventHandler
from utils.services import UserService


class Auth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.on_button_press.registerHandler("auth_button", EventHandler("auth", self.auth_handler, self.bot))

    @staticmethod
    async def auth_handler(bot, interaction):
        await interaction.respond(type=6)

        await interaction.author.send("Напишите мне в ответ свои логин и пароль от лк в формате: логин пароль")
        try:
            response = await bot.wait_for("message",
                                          timeout=60,
                                          check=lambda x: x.author.id == interaction.author.id
                                          )
        except futures.TimeoutError:
            await interaction.author.send("Время ожидания вышло. Повторите все шаги заново")
            return

        try:
            login, password = response.content.split()
        except ValueError:
            await interaction.author.send("Неверный логин или пароль. Попробуйте пройти авторизацию еще раз ")
            return

        user_info = await UserAuth.auth(interaction.guild, interaction.author, login, password)

        if user_info is not None:
            try:
                await UserService.saveUser(str(interaction.author.id), user_info['oneCGuid'])
            except UserAlreadyExists:
                pass


def setup(bot):
    bot.add_cog(Auth(bot))