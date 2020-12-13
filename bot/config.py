import os
import environ


# Build paths inside the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Environ
env_file = os.path.join(BASE_DIR, '.env')
environ.Env.read_env(env_file)


BOT_TOKEN = os.environ.get('BOT_TOKEN')

CHANNEL_ID = 787269607198818316

PREFIX = '/'

MAIN_COLOR = 0xd3597e

BOT_STATUS = [
'Пошел срать!',
'Кастую гейскую магию!!!'
]

HELLO_MESSAGES = [
'Hello1',
'Hello2',
'Hello3'
]
