from Bot import Bot
import os
from config import TOKEN

bot = Bot(TOKEN)

@bot.command()
async def load(ctx, extensions):
    bot.load_extension(f"cogs.{extensions}")
    await ctx.author.send("Done")


@bot.command()
async def unload(ctx, extensions):
    bot.unload_extension(f"cogs.{extensions}")
    await ctx.author.send("Done")


@bot.command()
async def reload(ctx, extensions):
    bot.unload_extension(f"cogs.{extensions}")
    bot.load_extension(f"cogs.{extensions}")
    await ctx.author.send("Done")


if __name__ == '__main__':
    bot.run()
