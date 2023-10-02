import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from itertools import cycle

load_dotenv()

client = commands.Bot(command_prefix=os.getenv('BOTPREFIX'), intents=discord.Intents.all())

@client.event
async def on_ready():
    print("bot is ready and booming!")
    await client.change_presence(activity=discord.Game(f"type {os.getenv('BOTPREFIX')}help for help"))

@client.command()
async def ping(ctx):
    await ctx.send("Hello there")


client.run(os.getenv('TOKEN'))