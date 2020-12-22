# Модуль sys
import sys

# Модуль logging
import logging

# Discord API
import discord
from discord.ext import commands, tasks

# Файл с настройками
from .config import *

# ------
from .utils import _random_choice


bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command('help')


@bot.event
async def on_ready():
    """
    Отправка приведственного сообщения на сервере при запуске бота
    и установка статуса.
    """
    await send_hello_message()
    change_bot_status.start()
    logging.info(f"{bot.user} в сети!")


@tasks.loop(minutes=30)
async def change_bot_status():
    """
    Смена статуса через определенный интервал времени.
    """
    await bot.change_presence(activity=discord.Game(_random_choice(list=BOT_STATUS)))


async def send_hello_message():
    """
    Отправка приветственного сообщения.
    """
    await bot.get_channel(CHANNEL_ID).send(_random_choice(list=HELLO_MESSAGES))


def _add_extension(bot):
    """
    Загрузка всех расширений (команд).
    """
    for extension in EXTENSIONS:
        try:
            bot.load_extension(extension)
        except Exception as error:
            logging.error(f"{extension} не может быть загружен. ------> {error}")


def run():
    """
    Запуск бота.
    """
    _add_extension(bot)
    if BOT_TOKEN == '':
        raise ValueError(
        "Отсутствует токен, введите токен своего приложения в файле /bot/config.py в BOT_TOKEN = 'token'"
        )
        sys.exit(1)
    bot.run(BOT_TOKEN)
