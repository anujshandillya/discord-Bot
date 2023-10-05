import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation.py is ready")

    # moderations using prefix commands.
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count:int):
        await ctx.channel.purge(limit=count)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, modreason):
        await ctx.guild.ban(member)
        conf=discord.Embed(title="Success!", color=discord.Color.orange())
        conf.add_field(name="Banned!",value=f"{member.display_name}({member.mention}) has been banned by {ctx.author.display_name}({ctx.author.mention})", inline=False)
        conf.add_field(name="Reason",value=modreason, inline=False)
        await ctx.send(embed=conf)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, modreason):
        await ctx.guild.kick(member)
        conf=discord.Embed(title="Success!", color=discord.Color.red())
        conf.add_field(name="Kicked!",value=f"{member.display_name}({member.mention}) has been kicked by {ctx.author.display_name}({ctx.author.mention})", inline=False)
        conf.add_field(name="Reason",value=modreason, inline=False)
        await ctx.send(embed=conf)

    @commands.command(name='unban')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userId):
        user=discord.Object(id=userId)
        await ctx.guild.unban(user)
        conf=discord.Embed(title="Success!", color=discord.Color.brand_green())
        conf.add_field(name="Unbanned!",value=f"<@{userId}> has been unbanned by {ctx.author.display_name}({ctx.author.mention})", inline=False)
        await ctx.send(embed=conf)

    @clear.error
    async def on_clear_error(self,ctx,e):
        if isinstance(e,commands.MissingPermissions):
            await ctx.send("Error❌: MiissingPermissions. You don't have permission to use this command.")
        if isinstance(e,commands.MissingRequiredArgument):
            await ctx.send("Error❌: MiissingRequiredArguments. You need to pass a whole number in order to run this command.")
        if isinstance(e,commands.BadArgument):
            await ctx.send("Error❌: BadArgument. You need to pass a whole number in order to run this command.")

    @ban.error
    async def on_ban_error(self,ctx,e):
        if isinstance(e,commands.MissingPermissions):
            await ctx.send("Error❌: MiissingPermissions. You don't have permission to use this command.")
        if isinstance(e,commands.MissingRequiredArgument):
            await ctx.send("Error❌: MissingRequiredArguments. You need to mention the userID or @mention in order to use this command.")

    @unban.error
    async def on_unban_error(self,ctx,e):
        if isinstance(e,commands.MissingPermissions):
            await ctx.send("Error❌: MiissingPermissions. You don't have permission to use this command.")
        if isinstance(e,commands.MissingRequiredArgument):
            await ctx.send("Error❌: MiissingRequiredArguments. You need to mention the userID or @mention in order to use this command.")

    @kick.error
    async def on_kick_error(self,ctx,e):
        if isinstance(e,commands.MissingPermissions):
            await ctx.send("Error❌: MiissingPermissions. You don't have permission to use this command.")
        if isinstance(e,commands.MissingRequiredArgument):
            await ctx.send("Error❌: MiissingRequiredArguments. You need to mention the userID or @mention in order to use this command.")

async def setup(client):
    await client.add_cog(Moderation(client))