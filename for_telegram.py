# >>>>>>>>>>>   IMPORTS   <<<<<<<<<<

from pyrogram import Client, filters
from pyrogram.types import Message, User
import requests


anime = Client(
    "BotNameHere",
    bot_token = "your bot token,
    api_id = your api id,
    api_hash = "your api hash"
)

 
url = "https://animechan.vercel.app/api/random"

@anime.on_message(filters.command("anime_quote"))   # u can change it to your own command 
def ani_q(bot,m:Message):
    data = requests.get(url).json()
    ani = data['anime']
    char = data['character']
    qu = data['quote']
    bot.send_message(text=f"**''{qu}''**\n\n-__{char}__ (__{ani}__)",chat_id=m.chat.id)
    
anime.run()
