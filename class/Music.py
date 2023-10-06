import discord
import os
import json
from discord.ext import commands
import asyncio
from asyncio import run_coroutine_threadsafe
import re
# import yt_dlp as youtube_dl
from yt_dlp import YoutubeDL
from urllib import parse, request


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.is_playing = {}
        self.is_paused = {}
        self.queue = {}
        self.queue_index = {}
        self.YTDL_OPTIONS = {
            'format': 'bestaudio/best',
            'outtmpl': 'music_files/%(id)s.mp3',
            'restrictfilenames': True,
            'noplaylist': True,
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'logtostderr': False,
            'quiet': True,
            'no_warnings': True,
            'default_search': 'auto',
            'source_address': '0.0.0.0'
        }
        self.FFMPEG_OPTIONS = {
            'options': '-vn'
        }

        self.embedBlue = 0x2c76dd
        self.embedRed = 0xdf1141
        self.embedGreen = 0x0eaa51

        self.vc = {}

    @commands.Cog.listener()
    async def on_ready(self):
        for guilds in self.client.guilds:
            id = int(guilds.id)
            self.queue[id] = []
            self.queue_index[id] = 0
            self.is_paused[id] = self.is_playing[id] = False
            self.vc[id] = None
        print("Music.py is ready.")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        id = int(member.guild.id)
        if member.id != self.client.user.id and before.channel != None and after.channel != before.channel:
            remainingChannelMembers = before.channel.members
            if len(remainingChannelMembers) == 1 and remainingChannelMembers[0].id == self.client.user.id and self.vc[id].is_connected():
                self.is_playing[id] = self.is_paused[id] = False
                self.queue[id] = []
                self.queue_index[id] = 0
                await self.vc[id].disconnect()

    def YT_search(self, search):
        query = parse.urlencode({'search_query': search})
        html = request.urlopen('https://www.youtube.com/results?'+query)
        res = re.findall('/watch\?v=(.{11})', html.read().decode())

        return res[0:10]

    def YT_ext(self, url):
        with YoutubeDL(self.YTDL_OPTIONS) as ytdl:
            try:
                info = ytdl.extract_info(url, download=False)
            except:
                return False
        return {
            'link': 'https://www.youtube.com/watch?v=' + url,
            'thumbnail': 'https://i.ytimg.com/vi/' + url + '/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD5uL4xKN-IUfez6KIW_j5y70mlig',
            'source': info['formats'][0]['url'],
            'title': info['title']
        }

    async def join_VC(self, ctx, channel):
        id = int(ctx.guild.id)
        if self.vc[id] == None or not self.vc[id].is_connected():
            self.vc[id] = await channel.connect()
            if self.vc[id] == None:
                await ctx.send("Could not connect to VC🥹")
                return
        else:
            await self.vc[id].move_to(channel)

    async def play_next(self, ctx):
        id = int(ctx.guild.id)
        if not self.is_playing:
            return
        if self.queue_index[id] < len(self.queue):
            self.is_playing = True
            self.queue_index[id] += 1

            song = self.queue[id][self.queue_index[id]][0]
            message = "agla suno"
            cor = ctx.send(message)
            rct = run_coroutine_threadsafe(cor, self.client.loop)
            try:
                rct.result()
            except:
                pass

            self.vc[id].play(discord.FFmpegPCMAudio(
                song['source'], **self.FFMPEG_OPTIONS
            ), after=lambda e: self.play_next(ctx))
        else:
            self.queue_index[id] += 1
            self.is_playing = False

    async def play_music(self, ctx):
        id = int(ctx.guild.id)
        if self.queue_index[id] < len(self.queue):
            self.is_playing[id] = True
            self.is_paused[id] = False

            await self.join_VC(ctx, self.queue[id][self.queue_index[id]][1])

            song = self.queue[id][self.queue_index[id]][0]
            message = "abhi ke liye yhi"
            await ctx.send(message)

            self.vc[id].play(discord.FFmpegPCMAudio(
                song['source'], **self.FFMPEG_OPTIONS
            ), after=lambda e: self.play_next(ctx))
        else:
            await ctx.send("The queue is empty.")
            self.queue_index[id] += 1
            self.is_playing[id] = False

    @commands.command(
        name="join",
        aliases=['connect', 'c'],
    )
    async def join(self, ctx):
        if ctx.author.voice:
            userchannel = ctx.author.voice.channel
            await self.join_VC(ctx, userchannel)
            await ctx.send(f"Connected to {userchannel}👍")
        else:
            await ctx.send("You need to be in a voice channel.🤕")

    @commands.command(
        name="leave",
        aliases=['disconnect'],
    )
    async def leave(self, ctx):
        id = int(ctx.guild.id)
        self.is_playing[id] = self.is_paused[id] = False
        self.queue[id] = []
        self.queue_index[id] = 0
        if self.vc != None:
            await ctx.send("See you 'round")
            await self.vc[id].disconnect()

    @commands.command(
        name="play",
        aliases=['p'],
    )
    async def play(self, ctx, *query):
        search = " ".join(query)
        id = ctx.guild.id
        try:
            channel = ctx.author.voice.channel
        except:
            await ctx.send("You are not connected to any voice channel.")

        if not query:
            if len(self.queue[id] == 0):
                await ctx.send("Queue is empty.")
                return
            elif not self.is_playing[id]:
                if self.queue[id] == None or self.vc[id] == None:
                    await self.play_music(ctx)
                else:
                    self.is_playing = True
                    self.is_paused = False
                    self.vc[id].resume()
            else:
                return
        else:
            song = self.YT_ext(self.YT_search(search)[0])
            if type(song) == type(True):
                await ctx.send("Could not play. tyr again.")
            else:
                self.queue[id].append([song, channel])

                if not self.is_playing[id]:
                    await self.play_music(ctx)
                else:
                    message = "Added to queue"
                    await ctx.send(message)


async def setup(client):
    await client.add_cog(Music(client))
