from pyrogram import Client
from config import Config
if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    data = Config()
    app = Client(
        "terabox",
        bot_token=data.BOT_TOKEN,
        api_id=data.API_ID,
        api_hash=data.API_HASH,
        plugins=plugins
    )
    app.run()