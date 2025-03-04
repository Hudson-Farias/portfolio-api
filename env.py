from dotenv import load_dotenv
from os import  getenv

load_dotenv()

ENV_PATH = getenv('ENV_PATH')
load_dotenv(ENV_PATH)

POSTGRES_HOST = getenv('POSTGRES_HOST')
POSTGRES_USER = getenv('POSTGRES_USER')
POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = getenv('POSTGRES_PORT')
POSTGRES_DB = getenv('POSTGRES_DB')
