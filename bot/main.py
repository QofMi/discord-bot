# Discord API
import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient

# YouTube API
import youtube_dl
from youtube import *

# Модуль random
from random import choice

# Файл с настройками
from config import *


bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command('help')
queue = []

@bot.event
async def on_ready():
    """
    Отправка приведственного сообщения на сервере при запуске бота
    и установка статуса.
    """
    await send_hello_message()
    change_bot_status.start()
    print('{0} is online'.format(bot.user))


@tasks.loop(minutes=30)
async def change_bot_status():
    """
    Смена статуса через определенный интервал времени, случайно выбирия из списка.
    """
    await bot.change_presence(activity=discord.Game(choice(BOT_STATUS)))


def _random_hello_message() -> str:
    """
    Вывод случайного сообщения из списка.
    """
    hello_message = choice(HELLO_MESSAGES)
    return hello_message


async def send_hello_message():
    """
    Отправка сообщения.
    """
    await bot.get_channel(CHANNEL_ID).send(_random_hello_message())


@bot.command()
async def help(ctx):
    """
    Команда "/help", отображает информацию о доступных командах.
    """
    help = discord.Embed(title='Информация о доступных командах.', color=MAIN_COLOR)

    help.add_field(name='QofMi', value='Разработчик этой хуйни', inline=True)

    help.add_field(name='qmblog.ru', value='Да да, рекламирую свой сайт.', inline=True)

    help.add_field(name='{}join'.format(PREFIX), value='Эта команда добавляет бота в голосовой канал', inline=False)

    help.add_field(name='{}leave'.format(PREFIX), value='Эта команда удаляет бота из голосового канала', inline=False)

    await ctx.send(embed=help)


@bot.command(name='join', help='Эта команда добавляет бота в голосовой канал')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("Голосовой канал пуст")
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command(name='leave', help='Эта команда удаляет бота из голосового канала')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()




# @bot.command(name='queue', help='This command adds a song to the queue')
# async def queue_(ctx, url):
#     global queue
#
#     queue.append(url)
#     await ctx.send(f'`{url}` added to queue!')
#
# @bot.command(name='remove', help='This command removes an item from the list')
# async def remove(ctx, number):
#     global queue
#
#     try:
#         del(queue[int(number)])
#         await ctx.send(f'Your queue is now `{queue}!`')
#
#     except:
#         await ctx.send('Your queue is either **empty** or the index is **out of range**')
#
# @bot.command(name='play', help='This command plays songs')
# async def play(ctx):
#     global queue
#
#     server = ctx.message.guild
#     voice_channel = server.voice_client
#
#     async with ctx.typing():
#         player = await YTDLSource.from_url(queue[0], loop=bot.loop)
#         voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
#
#     await ctx.send('**Now playing:** {}'.format(player.title))
#     del(queue[0])
#
# @bot.command(name='pause', help='This command pauses the song')
# async def pause(ctx):
#     server = ctx.message.guild
#     voice_channel = server.voice_client
#
#     voice_channel.pause()
#
# @bot.command(name='resume', help='This command resumes the song!')
# async def resume(ctx):
#     server = ctx.message.guild
#     voice_channel = server.voice_client
#
#     voice_channel.resume()
#
# @bot.command(name='view', help='This command shows the queue')
# async def view(ctx):
#     await ctx.send(f'Your queue is now `{queue}!`')
#
# @bot.command(name='stop', help='This command stops the song!')
# async def stop(ctx):
#     server = ctx.message.guild
#     voice_channel = server.voice_client
#
#     voice_channel.stop()


bot.run(BOT_TOKEN)
