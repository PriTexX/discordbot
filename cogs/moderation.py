import discord
from discord.ext import commands
from discord_components import Button, ButtonStyle
from guild import RoleManager


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
        embed = discord.Embed(
            title="Авторизация на дискорд сервере",
            url="https://e.mospolytech.ru/",
            color=0xFFFFFF,
            description="Следуйте инструкциям ниже, чтобы получить доступ к каналам Московского Политеха"
        )

        embed.add_field(name="1 шаг", value='Нажмите на кнопку "Авторизоваться"', inline=True)
        embed.add_field(name="3 шаг", value="Отправьте свои логин и пароль от личного кабинета", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=False)
        embed.add_field(name="2 шаг", value="Дождитесь сообщения от бота", inline=True)
        embed.add_field(name="4 шаг", value="Если авторизация не удалась, попробуйте повторить позже", inline=True)

        await ctx.send(
            embed=embed,
            components=[
                Button(style=ButtonStyle.green, label="Авторизоваться", custom_id="auth_button"),
            ]
        )

    @commands.command()
    async def sort(self, ctx):
        await ctx.channel.purge(limit=1)
        await RoleManager.sortRoles(ctx.author.guild)


def setup(bot):
    bot.add_cog(Moderation(bot))
