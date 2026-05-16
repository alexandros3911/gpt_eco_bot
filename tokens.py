import os

from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env

BOT_TOKEN = os.environ["BOT_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]