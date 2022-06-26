from Bot import Bot
TOKEN="OTg5OTMwNjYwNzc0OTUyOTkx.Gy1Dy0.HXhyeTReRy0EORKcp_nJw9GlfNB9TDvwjzpFHw"

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

bot.run()
