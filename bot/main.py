import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands, tasks
from datetime import datetime, timedelta
from pytz import timezone
global lot_num

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

list_of_suffix = {1: 'st', 2: 'nd', 3: 'rd'}

def ordinal(num):
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = list_of_suffix.get(num % 10, 'th')
    return str(num) + suffix

lot_dict = {1 : "Oscar",
            2 : "Gabbie",
            3 : "CJ",
            4 : "Babs",
            5 : "Soods",
            6 : "Russ",
            7 : "Wilma",
            8 : "Pat",
            9 : "Auste",
            10: "Joseph",
            11: "Charles",
            12: "Phil"}

with open("bot/counter.txt", "r") as file:
    lot_num = int(file.readline().rstrip())

temp_num = 1

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.event
async def on_message(message):
    
    for i in range(2,1000):
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
    
    elif 'sammus' in message.content and 'thank' in message.content:
        await message.channel.send('No problem 😊.')
    
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
        
    elif '🅿️' in message.content and 'sammus' in message.content:
        await message.channel.send('I am not sure what the definition of 🅿️ is.')
    
    elif 'sammus' in message.content and 'lotto' in message.content and 'this week' in message.content:
        if lot_num == 1:
            await message.channel.send('Ew, it\'s ' + lot_dict.get(lot_num) + ' this week 🤮.')
        else:
            await message.channel.send('Hello, it is ' + lot_dict.get(lot_num) + ' this week.')
        
    elif 'sammus' in message.content and 'lotto' in message.content and 'next week' in message.content:
        if lot_num == 12:
            temp_num = 1
        else:
            temp_num = lot_num + 1
        
        if temp_num == 1:
            await message.channel.send('Ew, it\'s ' + lot_dict.get(temp_num) + ' next week 🤮.')
        else:
            await message.channel.send('Hello, it is ' + lot_dict.get(temp_num) + ' next week.')
       
    elif message.author.id == 284562536378925058 and 'sammus' in message.content: 
        await message.channel.send('Sorry Gabbie, I am a disappointment to you. I do not know how to respond to that.')
    
    elif message.author.id == 284562536378925058 and 'hi' in message.content and 'sammus' in message.content:
        await message.channel.send('Hello, Gabbie.')

    elif message.author.id == 419361911319298058 and 'sammus' in message.content:
        await message.channel.send('Sorry Oscar, talk to the hand 🖐️.')
    
    elif 'sammus' in message.content:
        await message.channel.send('Sorry, I do not know how to respond to that.')

@tasks.loop(hours=24)
async def to_do():
    global lot_num
    est_tz = pytz.timezone('Canada/Eastern')

    if datetime.now(tz = est_tz).strftime("%d") == 01:
        await bot.get_channel(461601814673096713).send("Wake up, it's the first of the month.")
   
    if datetime.now(tz = est_tz).weekday() == 0:
        file = open("bot/counter.txt", "w")
        file.write(str(lot_num + 1))
        
        with open("bot/counter.txt", "r") as file:
            lot_num = int(file.readline().rstrip())
        
        if lot_num > 12:
            file = open("bot/counter.txt", "w")
            file.write(str(1))
            file.close()
        
        with open("bot/counter.txt", "r") as file:
            lot_num = int(file.readline().rstrip())
        
        await bot.get_channel(461601814673096713).send("Happy Monday, this week's lotto rotation is " + lot_dict.get(lot_num) + ".")        

@to_do.before_loop
async def before_to_do():
    await bot.wait_until_ready()
               
to_do.start()
bot.run(TOKEN)
