import discord
import random
import datetime
from discord.ext import tasks, commands
import os

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1408765577350086810

foods = [
    "カレー", "ラーメン", "オムライス", "寿司",
    "ハンバーグ", "唐揚げ", "うどん", "ピザ"
]

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot起動")
    lucky_food.start()

@tasks.loop(minutes=1)
async def lucky_food():
    now = datetime.datetime.now()

    if now.hour == 23 and now.minute == 00:
        channel = bot.get_channel(CHANNEL_ID)
        food = random.choice(foods)
        await channel.send(f"☀️ 今日のラッキーフードは **{food}** です！")

bot.run(TOKEN)
