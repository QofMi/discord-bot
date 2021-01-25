# Discord API
import discord
from discord.ext import commands

# Файл с настройками
from ..config import *

# Модуль logging
import logging

# commands
from ..commands import COMMANDS


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["h"])
    async def help(self, ctx):
        """
        Команда "help", отображает информацию о доступных командах.
        """
        help = discord.Embed(title='Информация о доступных командах.', color=MAIN_COLOR)
        help.add_field(name='QofMi', value='Разработчик этой хуйни', inline=True)
        help.add_field(name='qmblog.ru', value='Да да, рекламирую свой сайт.', inline=True)
        try:
            for i in COMMANDS:
                help.add_field(name=f'{PREFIX}{COMMANDS[i]["name"]} или {PREFIX}{COMMANDS[i]["aliases"]}', value=COMMANDS[i]["help"], inline=False)
        except Exception as error:
            logging.error(f"ERROR -------> {error}")
    
        await ctx.send(embed=help)


def setup(bot):
    bot.add_cog(Help(bot))
