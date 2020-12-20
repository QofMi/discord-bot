# Модуль random
from random import choice


def _random_choice(list: None) -> str:
    """
    Выбор случайного сообщения из списка.
    """
    random_message = choice(list)
    return random_message
