import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

list_of_suffix = {1: 'st', 2: 'nd', 3: 'rd'}

def ordinal(num):
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = list_of_suffix.get(num % 10, 'th')
    return str(num) + suffix

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.event
async def on_message(message):

    if message.author == client.user:
        return

    elif message.content.startswith('Hello, sammus'):
        await message.channel.send('Hello!')

    elif message.content.startswith('Introduce yourself, sammus'):
        await message.channel.send('Hi, my name is sammus and I am a bot made by Roch.')

    elif message.content.startswith('sammus, what day of the year is it?'):
        day_of_year = datetime.now().timetuple().tm_yday
        str_day = ordinal(day_of_year)
        await message.channel.send('Good morning, happy ' + str_day + ' day of the year.')
    
    elif 'sammus' in message.content and 'day' in message.content:
        day_of_year = datetime.now().timetuple().tm_yday
        str_day = ordinal(day_of_year)
        await message.channel.send('Were you asking for the day? It is the ' + str_day + ' day of the year.')

    elif '🅿️' in message.content:
      await message.channel.send('🅿️ is defined as parking.')
        
    elif message.author.id == 284562536378925058 and 'sammus' in message.content: 
      await message.channel.send('Sorry Gabbie, I am a disappointment to you. I do not know how to respond to that.')

    elif 'sammus' in message.content:
      await message.channel.send('Sorry, I do not know how to respond to that.')

@bot.command()
async def ping(ctx):
    await ctx.send("pong")



server.server()
bot.run(TOKEN)
