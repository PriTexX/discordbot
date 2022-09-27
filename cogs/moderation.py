import discord
from discord.ext import commands
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
    async def instruct(self, ctx):
        embed = discord.Embed(
            title="Авторизация на дискорд сервере",
            url="https://e.mospolytech.ru/",
            color=0xFFFFFF,
            description="Следуйте инструкциям ниже, чтобы получить доступ к каналам Московского Политеха"
        )

        embed.add_field(name="1 шаг", value='Перейдите* в личные сообщения к боту', inline=True)
        embed.add_field(name="2 шаг", value="Отправьте свои логин и пароль** от личного кабинета", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=False)
        embed.add_field(name="3 шаг", value="Следуйте указаниям бота", inline=True)
        embed.add_field(name="4 шаг", value="Если авторизация не удалась, попробуйте повторить позже", inline=True)

        embed.set_footer(text=
                              "* Чтобы попасть к боту в личку\n "
                              "На ПК: Нажмите правой кнопкой мыши по боту в чате и перейдите в Сообщения.\n "
                              "На телефоне: Нажмите по боту и перейдите в Сообщения\n\n"
                              "** Логин и пароль нужно отправлять в формате: логин пароль"
                         )

        await ctx.send(embed=embed)

    @commands.command()
    async def sort(self, ctx):
        if ctx.author.id != 229033111197843456:
            return

        await ctx.channel.purge(limit=1)
        await RoleManager.sortRoles(ctx.author.guild)


def setup(bot):
    bot.add_cog(Moderation(bot))
