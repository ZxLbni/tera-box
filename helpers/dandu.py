from pyrogram import Client, filters ,enums
from helpers.convertors import convert_size,convert_time,progress_text
from pyrogram.types import *
import requests
import time 
import math
import os

async def download(message,link,id,file_size,file_name):
    resp = requests.get(link,allow_redirects=True,stream=True)
    total_size  = file_size
    downloaded = 0
    start = elapsed = time.time()
    with open(f"{id}.mp4", 'wb') as f:
        for chunk in resp.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                if time.time() - elapsed > 3:
                    percentage = math.floor((downloaded/total_size)*100)
                    speed = downloaded / (time.time() - start)
                    eta = round((total_size - downloaded) / speed)
                    progress = await progress_text(downloaded,total_size)
                    speed = await convert_size(speed)
                    eta = await convert_time(eta)
                    text = f"Downloading To Server\n\n`{file_name}`\n\n"
                    text+= f"`{progress}` `( {percentage}% )`\n\n"
                    text+= f"**Progress**: `{await convert_size(downloaded)}`/`{await convert_size(total_size)}`\n\n"
                    text+= f"**Speed**: `{speed}/s`\n\n"
                    text+= f"**ETA**: `{eta}`"
                    elapsed = time.time()
                    await message.edit(text)
                else:
                    pass
    return f"{id}.mp4"
elapse_time = {}
async def upload(current,total,message,file_name,id):
    global elapse_time
    if current == total:
        try:
            elapse_time.pop(id)
        except:
            pass
    if id not in elapse_time:
        elapse_time[id] = time.time()
    else:
        if time.time() - elapse_time[id] > 3:
            elapse_time[id] = time.time()
            percentage = math.floor((current/total)*100)
            progress = await progress_text(current,total)
            text = f"Uploading To Telegram\n\n`{file_name}`\n\n"
            text+= f"`{progress}` `( {percentage}% )`\n\n"
            text+= f"**Progress**: `{await convert_size(current)}`/`{await convert_size(total)}`"
            await message.edit(text)
        else:
            pass