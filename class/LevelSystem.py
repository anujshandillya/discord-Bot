import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio
import json
import math
import random

load_dotenv()

afile=os.getenv('level')

class LevelSystem(commands.Cog):
    def __init__(self,client):
        self.client=client

        self.client.loop.create_task(self.save())

        with open(afile,'r') as f:
            self.users=json.load(f)

    def level_up(self,userID):
        current_exp=self.users[userID]["Experience"]
        current_level=self.users[userID]["Level"]

        if current_exp >= math.ceil((6*(current_level ** 4))/2.5):
            self.users[userID]["Level"]+=1
            return True
        else:
            return False

    async def save(self):
        await self.client.wait_until_ready()

        while not self.client.is_closed():
            with open(afile,'w') as f:
                json.dump(self.users,f,indent=4)

            await asyncio.sleep(5)

    @commands.Cog.listener()
    async def on_ready(self):
        print("LevelSystem.py is ready.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.client.user.id:
            return
        
        userID=str(message.author.id)

        if not userID in self.users:

            self.users[userID]={}
            self.users[userID]["Level"]=0
            self.users[userID]["Experience"]=0

        random_exp=random.randint(5,15)
        self.users[userID]["Experience"]+=random_exp

        if self.level_up(userID):

            levelUpEmbed=discord.Embed(title="WOO HOO!!!", color=discord.Color.random())
            levelUpEmbed.add_field(name="Congratulations🥳 on leveling up!!",value=f"{message.author.mention} has just levelled up to level {self.users[userID]['Level']}")

            await message.channel.send(embed=levelUpEmbed)

    @commands.command(aliases=['rank','lvl'])
    async def level(self,ctx,user: discord.User=None):
        if user is None:
            user=ctx.author
        elif user is not None: 
            user=user

        mesEmbed=discord.Embed(title=f"{user.name}'s Level & Experience",color=discord.Color.purple())
        mesEmbed.add_field(name="Level", value=f"Your level is {self.users[str(user.id)]['Level']}")
        mesEmbed.add_field(name="Experience", value=f"Your experience is {self.users[str(user.id)]['Experience']}")
        mesEmbed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
        await ctx.send(embed=mesEmbed)

    @commands.command(aliases=['rank0','lvl0'])
    async def levelreset(self,ctx):
        user=ctx.author

        self.users[str(user.id)]["Level"]=0
        self.users[str(user.id)]["Experience"]=0

        mesEmbed=discord.Embed(title=f"{user.name}'s Level & Experience Reset",color=discord.Color.dark_green())
        mesEmbed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
        await ctx.send(embed=mesEmbed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def resetmem(self,ctx,user:discord.User):
        self.users[str(user.id)]["Level"]=0
        self.users[str(user.id)]["Experience"]=0

        mesEmbed=discord.Embed(title=f"{user.name}'s Level & Experience Reset",color=discord.Color.dark_green())
        mesEmbed.set_footer(text=f"Admin: {ctx.author.name}",icon_url=ctx.author.avatar)
        await ctx.send(embed=mesEmbed)

    @resetmem.error
    async def on_error(self,ctx,e):
        if isinstance(e,commands.MissingPermissions):
            await ctx.send("Error❌: MiissingPermissions. You are not the administrator of this server. Contact the administrator.")
        if isinstance(e,commands.MissingRequiredArgument):
            await ctx.send("Error❌: MiissingRequiredArguments. You need to @mention user in order to run this command.")
        if isinstance(e,commands.BadArgument):
            await ctx.send("Error❌: BadArgument. You need to @mention user in order to run this command.")


    
async def setup(client):
    await client.add_cog(LevelSystem(client))