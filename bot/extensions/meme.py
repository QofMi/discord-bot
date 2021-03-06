# Discord API
import discord
from discord.ext import commands, tasks

# Файл с настройками
from ..config import CHANNEL_ID, MAIN_COLOR

# utils
from ..utils import _random_choice, _get_data

# Модуль logging
import logging


URL = "http://joyreactor.cc/tag/приколы+для+даунов/"

MEME_LIST = []

TITLE = []


def random_num_in_range() -> int:
    """
    Случайно выбирает число из диапазона.
    """
    data = list(range(1, 43))
    return _random_choice(data)


def get_image() -> str:
    """
    Парсит со случайной страницы, случайный пост с изображением.
    """
    find_image = _get_data(URL + str(random_num_in_range())).find_all("div", class_="image")
    for image in find_image:
        try:
            image_url = image.find("img").get("src")
            MEME_LIST.append(image_url)
        except AttributeError as error:
            logging.error(f"ERROR -------> {error}")
    return _random_choice(MEME_LIST)


def clear_list() -> None:
    try:
        MEME_LIST.clear()
    except Exception as error:
        logging.error(f"ERROR 'clear_list' -----> {error}")


class Meme(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.send_random_meme.start()

    @tasks.loop(hours=2)
    async def send_random_meme(self):
        try:
            meme = discord.Embed(title=_random_choice(TITLE), color=MAIN_COLOR)
            meme.set_image(url = get_image())

            await self.bot.get_channel(CHANNEL_ID).send(embed=meme)
            clear_list()
        except Exception as error:
            logging.error(f"ERROR -------> {error}")


def setup(bot):
    bot.add_cog(Meme(bot))
