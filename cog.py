import nextcord
import os
from nextcord.ext import commands
import aiohttp
import asyncio
from datetime import datetime

class APOD(commands.Cog, name="APOD"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def apod(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.nasa.gov/planetary/apod?api_key=z4VtSw6jVJcvt1FkXsusOPRpwHLatDWirJFvgY7K") as api:
                data=await api.json()
                apod_title=data["title"]
                apod_date=data["date"]
                apod_text=data["explanation"]
                apod_img=data["url"]
                apod_hqimg=data["hdurl"]
                em=nextcord.Embed(title=apod_title,description=apod_text,type="rich",colour=0x7649fe)
                em.add_field(name=apod_date,value="")
                em.add_field(name="You can get the high quality picture from this link below",value=apod_hqimg,inline=False)
                if not apod_img== "None":
                    em.set_image(url=apod_img)
                await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(APOD(bot))
