from os import environ
from helpers.cookie import parseCookieFile
class Config:
    API_ID = int(environ.get("API_ID", default=22419004))
    API_HASH = environ.get("API_HASH", default="34982b52c4a83c2af3ce8f4fe12fe4e1")
    BOT_TOKEN = environ.get("BOT_TOKEN", default="7422021508:AAFtk-0pr81oH53Io0JTwQse0ACxywF3v2o")
    COOKIES = parseCookieFile("cookies.txt")
    
