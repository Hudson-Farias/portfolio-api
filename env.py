from dotenv import load_dotenv
from os import  getenv

load_dotenv()

AUTH_APP_URL = getenv('AUTH_APP_URL')
GITHUB_ACCESS_TOKEN = getenv('GITHUB_ACCESS_TOKEN')

ENV_PATH = getenv('ENV_PATH')
load_dotenv(ENV_PATH)

POSTGRES_HOST = getenv('POSTGRES_HOST')
POSTGRES_USER = getenv('POSTGRES_USER')
POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = getenv('POSTGRES_PORT')
POSTGRES_DB = getenv('POSTGRES_DB')

REDIS_HOST = getenv('REDIS_HOST')
REDIS_PASSWORD = getenv('REDIS_PASSWORD')
REDIS_PORT = getenv('REDIS_PORT')
