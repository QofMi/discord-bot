# Файл с настройками
from .config import *


COMMANDS = {}


MUSIC = {
    "join": {
        "name": "join",
        "help": "Эта команда добавляет бота в голосовой канал.",
        "aliases": "j",
    },
    "leave": {
        "name": "leave",
        "help": "Эта команда удаляет бота из голосового канала.",
        "aliases": "l",
    },
    "queue": {
        "name": "queue",
        "help": "Эта команда добавляет трек в очередь.",
        "aliases": "q",
    },
    "remove": {
        "name": "remove",
        "help": "Эта команда удаляет трек из списка.",
        "aliases": "r",
    },
    "play": {
        "name": "play",
        "help": "Команда для проигрывания трека.",
        "aliases": "p",
    },
    "pause": {
        "name": "pause",
        "help": "Эта команда ставит трек на паузу.",
        "aliases": "ps",
    },
    "resume": {
        "name": "resume",
        "help": "Эта команда возобновляет трек.",
        "aliases": "rs",
    },
    "view": {
        "name": "view",
        "help": "Эта команда показывает список треков в очереди.",
        "aliases": "v",
    },
    "stop": {
        "name": "stop",
        "help": "Эта команда прекращает проигрывание музыки!",
        "aliases": "st",
    },
}


def gen_commands() -> None:
    if 'bot.extensions.music' in EXTENSIONS:
        COMMANDS.update(MUSIC)


gen_commands()
