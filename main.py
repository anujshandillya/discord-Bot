import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio
import json

load_dotenv()

bottoken=os.getenv('TOKEN')
afile=os.getenv('channel')

def getServerPrefix(client, message):
    with open(afile,'r') as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]

# commandprefix=os.getenv('BOTPREFIX')



# For creating custom help commands.
class customHelpComands(commands.HelpCommand):
    def __init__(self):
        super().__init__()
    
    async def send_bot_help(self, mapping):
        embed_message=discord.Embed(title="Help", description="All commands", color=discord.Color.green)

        embed_message.set_thumbnail(url=self.context.author.guild.icon)

        await self.get_destination().send(embed_message)
    
    async def send_cog_help(self, cog):
        return await super().send_cog_help(cog)
    
    async def send_group_help(self, group):
        return await super().send_group_help(group)
    
    async def send_command_help(self, command):
        return await super().send_command_help(command)

    
    
client = commands.Bot(command_prefix=getServerPrefix, intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.tree.sync()
    print("bot is ready and booming!")
    await client.change_presence(activity=discord.Game(f"type help command for help"))

@client.event
async def on_guild_join(guild):
    with open(afile,'r') as f:
        prefix = json.load(f)

    prefix[str(guild.id)]="."

    with open(afile,'w') as f:
        json.dump(prefix,f,indent=4)

@client.event
async def on_guild_remove(guild):
    with open(afile,'r') as f:
        prefix = json.load(f)

    prefix.pop(str(guild.id))

    with open(afile,'w') as f:
        json.dump(prefix,f,indent=4)

@client.command()
async def setprefix(ctx, *, modprefix: str):
    with open(afile,'r') as f:
        prefix = json.load(f)

    prefix[str(ctx.guild.id)]=modprefix

    with open(afile,'w') as f:
        json.dump(prefix,f,indent=4)


async def load():
    for filename in os.listdir("./class"):
        if filename.endswith(".py"):
            await client.load_extension(f"class.{filename[:-3]}")

async def main():
    async with client:
        try:
            await load()
            await client.start(bottoken)
        except KeyboardInterrupt:
            print("Exiting...")
        else:
            print("Exiting...")



asyncio.run(main())