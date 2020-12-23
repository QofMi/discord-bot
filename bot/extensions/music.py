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


queue = []


async def _get_voice_channel(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    return voice_channel


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join', help='Эта команда добавляет бота в голосовой канал.', aliases=["j"])
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

    @commands.command(name='leave', help='Эта команда удаляет бота из голосового канала.', aliases=["l"])
    async def leave(self, ctx):
        try:
            voice_client = ctx.message.guild.voice_client
            await voice_client.disconnect()
        except Exception as error:
            logging.info(f"ERROR -------> {error}")
            await ctx.send("Меня уже нет в голосовом чате!")

    @commands.command(name='queue', help='Эта команда добавляет трек в очередь.', aliases=["q"])
    async def queue_(self, ctx, url):
        global queue
        queue.append(url)
        await ctx.send(f'`{url}` трек добавлен в очередь!')

    @commands.command(name='remove', help='Эта команда удаляет трек из списка.', aliases=["r"])
    async def remove(self, ctx, number):
        global queue
        try:
            del(queue[int(number)])
            await ctx.send(f'Трек удален из списка`{queue}!`')
        except:
            await ctx.send('Список пуст')

    @commands.command(name='play', help='Команда для проигрывания трека.', aliases=["p"])
    async def play(self, ctx):
        global queue
        server = ctx.message.guild
        voice_channel = server.voice_client
        async with ctx.typing():
            player = await YTDLSource.from_url(queue[0], loop=self.bot.loop)
            voice_channel.play(player, after=lambda e: print('Ля, ну ты чаго наделал: %s' % e) if e else None)

        await ctx.send('**Сейчас играет:** {}'.format(player.title))
        del(queue[0])

    @commands.command(name='pause', help='Эта команда ставит трек на паузу.')
    async def pause(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.pause()

    @commands.command(name='resume', help='Эта команда возобновляет трек.')
    async def resume(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.resume()

    @commands.command(name='view', help='Эта команда показывает список треков в очереди.', aliases=["v"])
    async def view(self, ctx):
        await ctx.send(f'Треки в списке `{queue}!`')

    @commands.command(name='stop', help='Эта команда прекращает проигрывание музыки!')
    async def stop(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.stop()


def setup(bot):
    bot.add_cog(Music(bot))
