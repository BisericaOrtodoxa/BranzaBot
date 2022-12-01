import discord
from googlesearch import search
import os
import random
import re
from discord import option
import asyncio
import time
import base64

site= " wikipedia.org"
discord_token="duper secret bot code goes here"
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)
comanda="$branza"
intents = discord.Intents.default()
intents.message_content = True
#def rm_command(x,query): #my first command implementation, not using slash commands
#    query_2 = query.replace(x, "") + site
#    print("Search query: " + query_2)
#    return query_2

   
##########################
@bot.slash_command(name="google", description="Searches a website for the desired info",guild_ids=[1042811421718761606]) # this decorator makes a slash command
@option("website", description="Enter website",required=False,default = '')
@option("term", description="")
#options for the created command



async def google(ctx,term, website:str):#command that performs a Google search based on user input via slash command
    async with ctx.typing():
        for j in search(str(term)+" "+ str(website),num=1, stop=1):
            await ctx.respond(j)  
            
 #####################################        
@bot.slash_command(name="seconds", description="Set a timer in seconds",guild_ids=[1042811421718761606]) # this decorator makes a slash command
@option("seconds", description="Number of seconds")


async def timer(ctx,seconds:int):
        print("A timer was set. Duration: "+ str(seconds)+" seconds")
        await ctx.respond("Timer set to "+ str(seconds) + " seconds")
        #time.sleep(int(seconds))
        await asyncio.sleep(seconds)
        await ctx.respond("Time has passed")
# my implementation of a timer command(in seconds). I could make it so it takes days and hours but I'm too lazy

##########################
@bot.slash_command(name="b64_e", description="Encodes a string using base64",guild_ids=[1042811421718761606]) # base64 encode command
@option("string")

async def b64_e(ctx,string:str):
    async with ctx.typing():
        string_to_ascii = string.encode("utf8")
        base64_to_ascii = base64.b64encode(string_to_ascii)
        base64_string = base64_to_ascii.decode("utf8")
        await ctx.respond(base64_string)
            
 #####################################     

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "porn" in message.content:
        await message.channel.send("nu-i voie") 
    if "sus" in message.content:
        await message.reply('Among SUS', mention_author=False)




    
            
            
bot.run(discord_token)
