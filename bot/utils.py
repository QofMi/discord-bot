# Модуль random
from random import choice

# библиотека requests
import requests

# библиотека BeautifulSoup
from bs4 import BeautifulSoup


def _random_choice(list: None) -> str:
    """
    Выбор случайного сообщения из списка.
    """
    random_message = choice(list)
    return random_message


def _get_data(url: str) -> str:
    """
    Парсинг HTML
    """
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    return soup
