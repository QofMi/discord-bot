# Discord API
import discord
from discord.ext import commands, tasks

# Модуль logging
import logging

# utils
from ..utils import _random_choice


TRIGGER_MESSAGE = [
'',
]

MEM_MESSAGE = [
'',
]


async def send_message_on_trigger(message, trigger_message: None, message_list: None):
    for i in trigger_message:
        if i in message.content.lower():
            await message.channel.send(_random_choice(list=message_list))


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot:
            return

        await send_message_on_trigger(message, trigger_message=TRIGGER_MESSAGE, message_list=MEM_MESSAGE)


def setup(bot):
    bot.add_cog(Events(bot))
