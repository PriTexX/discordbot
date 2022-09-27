import discord
from discord.ext import commands
from utils.user import UserAuth
from exceptions import UserAlreadyExists
from components import EventHandler
from utils.services import UserService


class Auth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.bot.on_button_press.registerHandler("auth_button", EventHandler("auth", self.auth_handler, self.bot))
        self.bot.on_message_sent_event.registerHandler(EventHandler("auth", self.auth_handler, self.bot))

    @staticmethod
    async def auth_handler(bot, message: discord.Message):
        if message.channel.type != discord.ChannelType.private or message.author.bot:
            return

        try:
            login, password = message.content.split()
        except ValueError:
            await message.author.send("Неверный логин или пароль. Попробуйте пройти авторизацию еще раз ")
            return

        guild = bot.get_guild(879925656396378112)
        user_info = await UserAuth.auth(guild, await guild.fetch_member(message.author.id), login, password)

        if user_info is not None:
            try:
                await UserService.saveUser(str(message.author.id), user_info['oneCGuid'])
            except UserAlreadyExists:
                pass


def setup(bot):
    bot.add_cog(Auth(bot))
