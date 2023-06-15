from os import environ
from helpers.cookie import parseCookieFile
class Config:
    API_ID = int(environ.get("API_ID"))
    API_HASH = environ.get("API_HASH")
    BOT_TOKEN = environ.get("BOT_TOKEN")
    COOKIES = parseCookieFile("cookies.txt")
    