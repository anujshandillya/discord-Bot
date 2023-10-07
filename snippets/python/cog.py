from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello from the cog!')

    @commands.command()
    async def goodbye(self, ctx):
        await ctx.send('Goodbye from the cog!')

def setup(bot):
    bot.add_cog(ExampleCog(bot))
