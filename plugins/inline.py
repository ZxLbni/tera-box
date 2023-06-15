from pyrogram import Client, filters,enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helpers.extractor import terabox
from config import Config
import pymongo
from helpers.dandu import download,upload
import os


@Client.on_callback_query(filters.regex("tera-"))
async def callback(client, query_callback):
    id = query_callback.data.split("-")[-1]
    chat_id = query_callback.from_user.id
    if os.path.exists(f"{id}.mp4"):
        query_callback.message.delete()
        await Client.send_message(chat_id,"Hold On SomeOne is Downloading This File\nPlease try after few seconds",
                                      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="📥 Download Video",callback_data=f"tera-{id}")]]))
    else:
        direct_link, file_size, file_name = await terabox("https://teraboxapp.com/s/"+id)
        name= await download(query_callback.message,direct_link,id,file_size,file_name)
        await Client.send_video(chat_id=chat_id,video=name,caption=f"**{file_name}**\nJoin @yssprojects",progress=upload,progress_args=(filters.regex("pyrogram"),file_name,id))