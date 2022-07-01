import discord
from discord.ext import commands
from components import EventHandler
from components.handlers import ButtonPressEventHandler
import os


class Bot(commands.Bot):
    def __init__(self, token):
        self.token = token
        self.on_button_press = ButtonPressEventHandler()

        intents = discord.Intents.default()
        intents.emojis = False
        intents.integrations = False
        intents.webhooks = True
        intents.dm_reactions = False
        intents.guild_reactions = False
        intents.presences = False
        intents.members = True

        super().__init__(command_prefix='!', intents=intents)

    # def prepare(self):
    #     auth_btn_handler = EventHandler("auth", auth_handler)
    #     self.on_button_press.addHandler("auth_button", auth_btn_handler)

    def run(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")
        # self.prepare()
        super().run(self.token)