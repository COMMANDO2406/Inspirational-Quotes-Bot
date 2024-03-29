import discord
from discord.ext import commands
import subprocess

BOT_TOKEN = "BOT TOKEN"
# If you want to test out this bot you can read BOT_SETUP.md for instructions on how to run this

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        await inspire(message)

async def inspire(message):
    # Execute main.py to generate the quote and image
    subprocess.run(['python', 'main.py'])

    # Send the image as a file on Discord
    with open('Output.png', 'rb') as f:
        image_file = discord.File(f)
        await message.channel.send(file=image_file)

bot.run(BOT_TOKEN)
