import os
import time
from datetime import datetime
import psutil
from pyrogram import Client, filters
from pyrogram.types import Message
from Yukki import BOT_USERNAME, MUSIC_BOT_NAME, app, boottime
from Yukki.Utilities.ping import get_readable_time
__MODULE__ = "Ping"
__HELP__ = """
/ping - Check if Bot is alive or not.
"""

# ===============================================
normaltext = "1234567890."
pingfont = [
    "𝟭",
    "𝟮",
    "𝟯",
    "𝟰",
    "𝟱",
    "𝟲",
    "𝟳",
    "𝟴",
    "𝟵",
    "𝟬",
    "•",
]

# ===============================================

async def bot_sys_stats():
    bot_uptime = int(time.time() - boottime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    stats = f"""
Uptime: {get_readable_time((bot_uptime))}
CPU: {cpu}%
RAM: {mem}%
Disk: {disk}%"""
    return stats
@app.on_message(filters.command(["ping", f"ping@{BOT_USERNAME}"]))
async def ping(_, message):
    start = datetime.now()
    response = await message.reply_photo(
        photo="Utils/Query.jpg",
        caption="`Pinging!...`",
    )
    uptime = await bot_sys_stats()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    resp = str((end - start).microseconds / 1000)
    for normal in resp:
        if normal in normaltext:
            pingchars = pingfont[normaltext.index(normal)]
            resp = resp.replace(normal, pingchars)    
    await response.edit_text(
        f"{resp} ms | {MUSIC_BOT_NAME}\n System Stats:</u></b>{uptime}"
    )
