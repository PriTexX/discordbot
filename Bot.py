import discord
from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.emojis = False
        intents.integrations = False
        intents.webhooks = True
        intents.dm_reactions = False
        intents.guild_reactions = False
        intents.presences = False
        intents.members = True

        super().__init__(command_prefix='!', intents=intents)
