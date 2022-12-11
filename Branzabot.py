import discord
from googlesearch import search
import os
import random
import re
from discord import option
import asyncio
import time
import base64

square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
site = " wikipedia.org"
discord_token = "*super cool discord bot token here*"
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)
comanda = "$branza"
intents = discord.Intents.default()
intents.message_content = True


# def rm_command(x,query): #my first command implementation, not using slash commands
#    query_2 = query.replace(x, "") + site
#    print("Search query: " + query_2)
#    return query_2


##########################
@bot.slash_command(name="google", description="Searches a website for the desired info",
                   guild_ids=[1042811421718761606])  # this decorator makes a slash command
@option("website", description="Enter website", required=False, default='')
@option("term", description="")
# options for the created command

async def google(ctx, term,
                 website: str):  # command that performs a Google search based on user input via slash command
    async with ctx.typing():
        for j in search(str(term) + " " + str(website), num=1, stop=1):
            await ctx.respond(j)

            #####################################


@bot.slash_command(name="seconds", description="Set a timer in seconds",
                   guild_ids=[1042811421718761606])  # this decorator makes a slash command
@option("seconds", description="Number of seconds")
async def timer(ctx, seconds: int):
    print("A timer was set. Duration: " + str(seconds) + " seconds")
    await ctx.respond("Timer set to " + str(seconds) + " seconds")
    # time.sleep(int(seconds))
    await asyncio.sleep(seconds)
    await ctx.respond("Time has passed")


# my implementation of a timer command(in seconds). I could make it so it takes days and hours but I'm too lazy

##########################
@bot.slash_command(name="b64_e", description="Encodes a string using base64",
                   guild_ids=[1042811421718761606])  # base64 encode command
@option("string")
async def b64_e(ctx, string: str):
    async with ctx.typing():
        string_to_ascii = string.encode("utf8")
        base64_to_ascii = base64.b64encode(string_to_ascii)
        base64_string = base64_to_ascii.decode("utf8")
        await ctx.respond(base64_string)


#####################################
@bot.slash_command(name="x_or_o", description="Play X and O!", guild_ids=[1042811421718761606])
@option("x_or_o", choices=["X", "O"])
@option("square_number")
@option("reset", description="empties the board", required=False, choices=["yes"])
@bot.event
async def xor0(ctx, x_or_o: str, square_number: int, reset):
    global square_1
    global square_2
    global square_3
    global square_4
    global square_5
    global square_6
    global square_7
    global square_8
    global square_9
    async with ctx.typing():
        def number_to_emoji(a):
            if a == 1:
                return ("❌")
            elif a == 2:
                return ("⭕")
            else:
                return ("◼️")
        def win_state():	# defines each winning state, im sure there was a better ay to do this but im not smart 
            if square_1 == square_2 and square_2 == square_3 and square_3 == 1:
                return "win x"
            if square_4 == square_5 and square_5 == square_6 and square_6 == 1:
                return "win x"
            if square_7 == square_8 and square_8==square_9 and square_9 == 1:
                return "win x"
            if square_1==square_5 and square_5==square_9 and square_9 == 1:
                return "win x"
            if square_3==square_5 and square_5==square_7 and square_7 ==1:
                return "win x"
            
            
            if square_1 == square_2 and square_2 == square_3 and square_3 == 2:
                return "win o"
            if square_4 == square_5 and square_5 == square_6 and square_6 == 2:
                return "win o"
            if square_7 == square_8 and square_8 == square_9 and square_9 == 2:
                return "win o"
            if square_1 == square_5 and square_5 == square_9 and square_9 == 2:
                return "win o"
            if square_3 == square_5 and square_5 == square_7 and square_7 == 2:
                return "win o"
            
        if x_or_o == "X" or x_or_o == "x":
            if reset == "yes":
                square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
            
            elif square_number == 1:   
                if reset !="yes":
                	square_1 = 1

            elif square_number == 2:
          
                if reset !="yes":
                	square_2 = 1
   
            elif square_number == 3:
                
                if reset !="yes":	
                    square_3 = 1
   
            elif square_number == 4:
                
                if reset !="yes":
                	square_4 = 1
    
            elif square_number == 5:
                
                if reset !="yes":
                	square_5 = 1
 
            elif square_number == 6:
                
                if reset !="yes":
                	square_6 = 1

            elif square_number == 7:
                
                if reset !="yes":
                	square_7 = 1
 
            elif square_number == 8:
                
                if reset !="yes":
                	square_8 = 1
   
            elif square_number == 9:     
                if reset !="yes":
                	square_9 = 1
     
                    
    
            else:
                await ctx.respond("Invalid square number")#place emoji for x	#place emoji for X
        if x_or_o == "O" or x_or_o == "o":
            if reset == "yes":
                square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
            
            elif square_number == 1:   
                if reset !="yes":
                	square_1 = 2

            elif square_number == 2:
          
                if reset !="yes":
                	square_2 = 2
   
            elif square_number == 3:
                
                if reset !="yes":	
                    square_3 = 2
   
            elif square_number == 4:
                
                if reset !="yes":
                	square_4 = 2
    
            elif square_number == 5:
                
                if reset !="yes":
                	square_5 = 2
 
            elif square_number == 6:
                
                if reset !="yes":
                	square_6 = 2

            elif square_number == 7:
                
                if reset !="yes":
                	square_7 = 2
 
            elif square_number == 8:
                
                if reset !="yes":
                	square_8 = 2
   
            elif square_number == 9:     
                if reset !="yes":
                	square_9 = 2#place emoji for 0
    await ctx.respond(number_to_emoji(square_1) + number_to_emoji(square_2) + number_to_emoji(square_3) + "\n" + number_to_emoji(
        square_4) + number_to_emoji(square_5) + number_to_emoji(square_6) + "\n" + number_to_emoji(
        square_7) + number_to_emoji(square_8) + number_to_emoji(square_9))	#send the state of the board after each move
    if win_state() == "win x":		#checks if x won
        await ctx.channel.send("X won! Resetting board")
        square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    if win_state() == "win o":		#checks if y won
        await ctx.channel.send("O won! Resetting board")
        square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
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

