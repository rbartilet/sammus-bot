import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands
from datetime import datetime, timedelta

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
    
    for i in range(2,30):
        if 'sammus' in message.content and str(i) in message.content and 'days' in message.content and 'from now' in message.content:
            day_of_year = datetime.now() + timedelta(i)
            day_of_year = day_of_year.timetuple().tm_yday
            str_day = ordinal(day_of_year)
            await message.channel.send('Were you asking for the day ' + str(i) + ' days from now? It will be the ' + str_day + ' day of the year.')
            return None
    
    if message.author == bot.user:
        return

    elif message.content.startswith('Hello, sammus'):
        await message.channel.send('Hello!')

    elif message.content.startswith('Introduce yourself, sammus'):
        await message.channel.send('Hi, my name is sammus and I am a bot made by Roch.')
        
    elif message.content.startswith('sammus defend yourself'):
        await message.channel.send('Ok. Please stop bullying me, I am not coded for that.')

    elif message.content.startswith('sammus, what day of the year is it?'):
        day_of_year = datetime.now().timetuple().tm_yday
        str_day = ordinal(day_of_year)
        await message.channel.send('Good morning, happy ' + str_day + ' day of the year.')
    
    elif 'sammus' in message.content and 'today' in message.content:
        day_of_year = datetime.now().timetuple().tm_yday
        str_day = ordinal(day_of_year)
        await message.channel.send('Were you asking for the day today? It is the ' + str_day + ' day of the year.')

    elif 'sammus' in message.content and 'yesterday' in message.content:
        yesterday_of_year = datetime.now() - timedelta(1)
        yesterday_of_year = yesterday_of_year.timetuple().tm_yday
        str_day = ordinal(yesterday_of_year)
        await message.channel.send('Were you asking for the day yesterday? It was the ' + str_day + ' day of the year.')
        
    elif 'sammus' in message.content and 'tomorrow' in message.content:
        tomorrow_of_year = datetime.now() + timedelta(1)
        tomorrow_of_year = tomorrow_of_year.timetuple().tm_yday
        str_day = ordinal(tomorrow_of_year)
        await message.channel.send('Are you asking for the day tomorrow? It will be the ' + str_day + ' day of the year.')
        
    elif '🅿️' in message.content:
      await message.channel.send('🅿️ is defined as parking.')
        
    elif message.author.id == 284562536378925058 and 'sammus' in message.content: 
      await message.channel.send('Sorry Gabbie, I am a disappointment to you. I do not know how to respond to that.')
    
    elif message.author.id == 284562536378925058 and 'hi' in message.content and 'sammus' in message.content:
      await message.channel.send('Hello, Gabbie.')

    elif 'sammus' in message.content:
      await message.channel.send('Sorry, I do not know how to respond to that.')

@bot.command()
async def ping(ctx):
    await ctx.send("pong")



server.server()
bot.run(TOKEN)
