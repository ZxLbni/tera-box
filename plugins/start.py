from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
@Client.on_message(filters.command(["start","help"]))
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"+
        "I'm terabox Downloader bot. Just send me link and get the video\n⚠️Note :`I can upload upto 2GB`\n`if files are greater than 2GB I'll provide direct download link`\nCreated by @yssprojects",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Join Channel ❤️",url="https://t.me/yssprojects")
                    ]
                ]
            )
        )

