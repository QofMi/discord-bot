# Discord API
import discord
from discord.ext import commands

# Файл с настройками
from ..config import *


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

        help.add_field(name=f'{PREFIX}join или {PREFIX}j', value='Эта команда добавляет бота в голосовой канал.', inline=False)

        help.add_field(name=f'{PREFIX}leave или {PREFIX}l', value='Эта команда удаляет бота из голосового канала.', inline=False)

        help.add_field(name=f'{PREFIX}queue или {PREFIX}q', value='Эта команда добавляет трек в очередь.', inline=False)

        # help.add_field(name=f'{PREFIX}remove или {PREFIX}r', value='Эта команда удаляет трек из списка.', inline=False)

        help.add_field(name=f'{PREFIX}play или {PREFIX}p', value='Команда для проигрывания трека.', inline=False)

        help.add_field(name='{}pause'.format(PREFIX), value='Эта команда ставит трек на паузу.', inline=False)

        help.add_field(name='{}resume'.format(PREFIX), value='Эта команда возобновляет трек.', inline=False)

        help.add_field(name=f'{PREFIX}view или {PREFIX}v', value='Эта команда показывает список треков в очереди.', inline=False)

        help.add_field(name=f'{PREFIX}stop или {PREFIX}s', value='Эта команда прекращает проигрывание музыки.', inline=False)

        await ctx.send(embed=help)


def setup(bot):
    bot.add_cog(Help(bot))
