import discord
from discord.ext import commands
from discord import app_commands

class Slash(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Slash.py is ready")

    @app_commands.command(name="ping",description="returns ping")
    async def ping(self,ctx: discord.Integration):
        botLatency=round(self.client.latency*1000)
        await ctx.response.send_message(f"{botLatency}ms")

async def setup(client):
    await client.add_cog(Slash(client))