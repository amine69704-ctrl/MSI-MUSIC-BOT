import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "YOUR_BOT_TOKEN_HERE"
VOICE_CHANNEL_ID = YOUR_VOICE_CHANNEL_ID_HERE

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if channel:
        if not channel.guild.voice_client:
            await channel.connect()

bot.run(TOKEN)
