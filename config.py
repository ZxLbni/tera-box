from os import environ
from helpers.cookie import parseCookieFile
class Config:
    API_ID = int(environ.get("API_ID", default=3847632))
    API_HASH = environ.get("API_HASH", default="1a9708f807ddd06b10337f2091c67657")
    BOT_TOKEN = environ.get("BOT_TOKEN", default="6312969509:AAE4CYabaJQceMV1fB3fRFRnbDRljk_je_c")
    COOKIES = parseCookieFile("cookies.txt")
    
