from pyrogram import Client, filters ,enums
from helpers.extractor import terabox
from helpers.convertors import convert_size
from pyrogram.types import *

@Client.on_message(filters.regex(r'https?://teraboxapp\.com/[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    id = link.split("/")[-1]
    chat_id = message.chat.id
    await bot.send_chat_action(chat_id, enums.ChatAction.TYPING)
    direct_link, file_size, file_name = await terabox(link)
    if file_size < 2097152000:
        inline_mode = InlineKeyboardButton(text="📥 Download Video",callback_data=f"tera-{id}")
    else:
        inline_mode = InlineKeyboardButton(text="📥 Download Video",url=direct_link)
    await message.reply_text(f"{file_name}\n\n**Size:** {await convert_size(file_size)}\n**Direct Link:** [{file_name}]({direct_link})",reply_markup=InlineKeyboardMarkup([[inline_mode]]),quote=True)
    
    