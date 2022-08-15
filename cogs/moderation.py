import discord
from discord.ext import commands
from discord_components import Button, ButtonStyle


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        if amount < 1: amount = 1

        await ctx.channel.purge(limit=amount + 1)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def putAuthButtonHere(self, ctx):
        await ctx.send(
            embed=discord.Embed(title="Авторизация"),
            components=[
                Button(style=ButtonStyle.green, label="Авторизоваться", custom_id="auth_button"),
            ]
        )


def setup(bot):
    bot.add_cog(Moderation(bot))
