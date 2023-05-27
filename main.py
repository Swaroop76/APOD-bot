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

key='OTQ3NjgyNTU2NTU0Mzk1Njk5.GOa0Bd.1AbprG_65F80vxyGDvZn7wZMtUTkx47Ccj_iMA'
bot.run(key)