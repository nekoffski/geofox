from discord.ext import commands


class Core(commands.Cog):
    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.channel.send("TODO")

    @commands.command()
    async def me(self, ctx: commands.Context):
        me_msg = "Foxes & Geologists discord bot, implemented in python3.9 & discord.py with <3 by nyeko and spułka"
        await ctx.channel.send(me_msg)
