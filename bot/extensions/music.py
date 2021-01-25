# Discord API
import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient

# YouTube API
import youtube_dl
from ..youtube import *

# Модуль logging
import logging

# config
from ..config import PREFIX

# commands
from ..commands import MUSIC


queue = []


async def _get_voice_channel(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    return voice_channel


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name=MUSIC["join"]["name"], help=MUSIC["join"]["help"], aliases=[MUSIC["join"]["aliases"]])
    async def join(self, ctx):
        user = ctx.message.author
        try:
            if not user.voice:
                await ctx.send(f"Ты не в голосовом чате! Зайди и попробуй снова -------> {PREFIX}join или {PREFIX}j.")
                return
            else:
                channel = ctx.message.author.voice.channel
                await channel.connect()
        except Exception as error:
            logging.info(f"ERROR -------> {error}")
            await ctx.send("Я уже в голосов чате, даун!")

    @commands.command(name=MUSIC["leave"]["name"], help=MUSIC["leave"]["help"], aliases=[MUSIC["leave"]["aliases"]])
    async def leave(self, ctx):
        try:
            voice_client = ctx.message.guild.voice_client
            await voice_client.disconnect()
        except Exception as error:
            logging.info(f"ERROR -------> {error}")
            await ctx.send("Меня уже нет в голосовом чате!")

    @commands.command(name=MUSIC["queue"]["name"], help=MUSIC["queue"]["help"], aliases=[MUSIC["queue"]["aliases"]])
    async def queue_(self, ctx, url):
        global queue
        queue.append(url)
        await ctx.send(f'`{url}` трек добавлен в очередь!')

    @commands.command(name=MUSIC["remove"]["name"], help=MUSIC["remove"]["help"], aliases=[MUSIC["remove"]["aliases"]])
    async def remove(self, ctx, number):
        global queue
        try:
            del(queue[int(number)])
            await ctx.send(f'Трек удален из списка`{queue}!`')
        except:
            await ctx.send('Список пуст')

    @commands.command(name=MUSIC["play"]["name"], help=MUSIC["play"]["help"], aliases=[MUSIC["play"]["aliases"]])
    async def play(self, ctx):
        global queue
        server = ctx.message.guild
        voice_channel = server.voice_client
        async with ctx.typing():
            player = await YTDLSource.from_url(queue[0], loop=self.bot.loop)
            voice_channel.play(player, after=lambda e: print('Ля, ну ты чаго наделал: %s' % e) if e else None)

        await ctx.send('**Сейчас играет:** {}'.format(player.title))
        del(queue[0])

    @commands.command(name=MUSIC["pause"]["name"], help=MUSIC["pause"]["help"], aliases=[MUSIC["pause"]["aliases"]])
    async def pause(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.pause()

    @commands.command(name=MUSIC["resume"]["name"], help=MUSIC["resume"]["help"], aliases=[MUSIC["resume"]["aliases"]])
    async def resume(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.resume()

    @commands.command(name=MUSIC["view"]["name"], help=MUSIC["view"]["help"], aliases=[MUSIC["view"]["aliases"]])
    async def view(self, ctx):
        await ctx.send(f'Треки в списке `{queue}!`')

    @commands.command(name=MUSIC["stop"]["name"], help=MUSIC["stop"]["help"], aliases=[MUSIC["stop"]["aliases"]])
    async def stop(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.stop()


def setup(bot):
    bot.add_cog(Music(bot))
