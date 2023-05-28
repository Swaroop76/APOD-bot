import os
import requests 
import nextcord
import logging
import json
from replit import db
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from typing import List
from nextcord import Intents

my_intents = Intents.default()
my_intents.message_content = True

bot = commands.Bot(command_prefix='#',intents=my_intents)

@bot.event
async def on_ready():
  print("We logged in as {0.user}".format(bot))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    
for folder in os.listdir("modules"):
    if os.path.exists(os.path.join("modules", folder, "cog.py")):
        bot.load_extension(f"modules.{folder}.cog")

key=#Mention your bot token with quotation marks here
bot.run(key)
