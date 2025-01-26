# This is a chatbot that connects to your Discord channel, reads all input, waits for "Marco" and responds "Polo".
# It is minimalistic to be a good tutorial so you see how it most basically works.
# All you need is to enter your channel ID in the last line

import discord
from discord.ext import commands

# Set up the bot
intents = discord.Intents.all()
intents.messages = True  # Enable message intent
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# Event: Respond to "Marco"
@bot.event
async def on_message(message):
    print("saw something")
    print(message)
    print("Content: ")
    print(message.content.lower())

    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    # Check for "Marco" and reply "Polo"
    if message.content.lower() == "marco":
        await message.channel.send("Polo")

    # Allow other commands to process
    await bot.process_commands(message)

# Run the bot
bot.run("replace with your channel ID, for me, this has 73 characters")
