import discord
from googlesearch import search
import re
from discord import option
import asyncio
import time
import base64
import os
from datetime import datetime
from discord.ext import commands


game_squares = {
    "square_1": 0, "square_2": 0, "square_3": 0, "square_4": 0, "square_5": 0, "square_6": 0, "square_7": 0,
    "square_8": 0, "square_9": 0,
}
square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
site = " wikipedia.org"
discord_token = " bot token here"
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)
intents = discord.Intents.default()
intents.message_content = True
number_emotes = ("1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟")
number_of_options_xrd=-1
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
    global game_squares
    async with ctx.typing():
        def board_reset():
            game_squares["square_1"], game_squares["square_2"], game_squares["square_3"], game_squares["square_4"], \
            game_squares["square_5"], game_squares["square_6"], game_squares["square_7"], game_squares["square_8"], \
            game_squares["square_9"] = 0, 0, 0, 0, 0, 0, 0, 0, 0

        def number_to_emoji(a):
            if a == 1:
                return ("❌")
            elif a == 2:
                return ("⭕")
            else:
                return ("◼️")

        def win_state(
                square_X_O):  # defines each winning state, im sure there was a better ay to do this but im not smart
            if game_squares["square_1"] == game_squares["square_2"] and game_squares["square_2"] == game_squares[
                "square_3"] and game_squares["square_3"] == square_X_O:
                return "win"
            if game_squares["square_4"] == game_squares["square_5"] and game_squares["square_5"] == game_squares[
                "square_6"] and game_squares["square_6"] == square_X_O:
                return "win"
            if game_squares["square_7"] == game_squares["square_8"] and game_squares["square_8"] == game_squares[
                "square_9"] and game_squares["square_9"] == square_X_O:
                return "win"
            if game_squares["square_1"] == game_squares["square_5"] and game_squares["square_5"] == game_squares[
                "square_9"] and game_squares["square_9"] == square_X_O:
                return "win"
            if game_squares["square_3"] == game_squares["square_5"] and game_squares["square_5"] == game_squares[
                "square_7"] and game_squares["square_7"] == square_X_O:
                return "win"

        def square_changer(one_or_two):
            if reset == "yes":
                board_reset()

            elif square_number == 1:
                if reset != "yes":
                    game_squares["square_1"] = one_or_two

            elif square_number == 2:

                if reset != "yes":
                    game_squares["square_2"] = one_or_two

            elif square_number == 3:

                if reset != "yes":
                    game_squares["square_3"] = one_or_two

            elif square_number == 4:

                if reset != "yes":
                    game_squares["square_4"] = one_or_two

            elif square_number == 5:

                if reset != "yes":
                    game_squares["square_5"] = one_or_two

            elif square_number == 6:

                if reset != "yes":
                    game_squares["square_6"] = one_or_two

            elif square_number == 7:

                if reset != "yes":
                    game_squares["square_7"] = one_or_two

            elif square_number == 8:

                if reset != "yes":
                    game_squares["square_8"] = one_or_two

            elif square_number == 9:
                if reset != "yes":
                    game_squares["square_9"] = one_or_two

            else:
                ctx.respond("Invalid square number")

        if x_or_o == "X" or x_or_o == "x":
            square_changer(1)
        if x_or_o == "O" or x_or_o == "o":
            square_changer(2)
    await ctx.respond(
        number_to_emoji(game_squares["square_1"]) + number_to_emoji(game_squares["square_2"]) + number_to_emoji(
            game_squares["square_3"]) + "\n" + number_to_emoji(
            game_squares["square_4"]) + number_to_emoji(game_squares["square_5"]) + number_to_emoji(
            game_squares["square_6"]) + "\n" + number_to_emoji(
            game_squares["square_7"]) + number_to_emoji(game_squares["square_8"]) + number_to_emoji(
            game_squares["square_9"]))  # send the state of the board after each move
    if win_state(1) == "win":  # checks if x won
        await ctx.channel.send("X won! Resetting board")
        board_reset()
    if win_state(2) == "win":  # checks if y won
        await ctx.channel.send("O won! Resetting board")
        board_reset()


#####################################

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


###################################### message logging. logs:messages sent, deleted and edited and stores them into msg_logs.txt. Upon request via slash command, this file is uploaded to discord
@bot.slash_command(name="logs", description="Fetch the logs from the stored file(the bot messages are not stored)",
                   guild_ids=[1042811421718761606])  # this decorator makes a slash command
async def logs(ctx):
    print("The logs command was run")
    logs = open("msg_logs.txt", "r")
    await ctx.respond(file=discord.File('msg_logs.txt'))
    logs.close


@bot.listen()
async def on_message_delete(message):
    logs = open("msg_logs.txt", "a")
    logs.write("\n" + "The following message was deleted" + "(" + str(datetime.now()) + "): " + str(
        message.content) + "   channel: " + str(message.channel.mention))
    print("The following message was deleted: " + str(message.content) + " channel: " + str(message.channel.mention))
    logs.close


@bot.listen()
async def on_message_edit(before, after):
    logs = open("msg_logs.txt", "a")
    logs.write("\n" + "The following message was edited" + "(" + str(datetime.now()) + "): " + str(
        before.content) + "    |edited to :" + " " + str(after.content) + "   channel: " + str(after.channel.mention))
    print("The following message was edited: " + str(before.content) + " channel: " + str(before.channel.mention))
    logs.close



    logs = open("msg_logs.txt", "a")
    logs.write("\n" + str(message.author) + "(" + str(message.created_at) + ")" + ": " + str(
        message.content) + "   channel: " + str(message.channel.mention))
    print("The following message was logged: " + str(message.content) + " written by " + str(
        message.author) + " channel: " + str(message.channel.mention))
    logs.close
    print("Logs file size: " + str(os.path.getsize("msg_logs.txt")))
    if int(os.path.getsize("msg_logs.txt")) > 10000:
        logs = open("msg_logs.txt", "r")
        await message.channel.send("Logs file size limit exceeded, sending logs then deleting server copy")
        await message.channel.send(file=discord.File('msg_logs.txt'))
        await os.remove("demofile.txt")
        logs.close

    if "porn" in message.content:
        await message.channel.send("nu-i voie")
    if "sus" in message.content:
        await message.reply('Among SUS', mention_author=False)


######################################
@bot.slash_command(name="poll", description="Make a poll", guild_ids=[1042811421718761606])
@option("option_1", default='')
@option("option_2", default='')
@option("option_3", required=False, default='')
@option("option_4", required=False, default='')
@option("option_5", required=False, default='')
@option("option_6", required=False, default='')
@option("option_7", required=False, default='')
@option("option_8", required=False, default='')
@option("option_9", required=False, default='')
@option("option_10", required=False, default='')

@bot.event
async def poll(ctx, option_1:str, option_2:str, option_3:str, option_4:str, option_5:str, option_6:str, option_7:str, option_8:str, option_9:str,option_10:str):
    number_emotes = ("1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟")
    def option_handler(x):
        option_list = [option_1, option_2, option_3, option_4, option_5, option_6, option_7, option_8,option_9, option_10]
        if option_list[x-1] != "":
            return str(option_list[x-1] + '\n\n')
        
        if option_list[x-1] == "": 
            return("")
        
    await ctx.respond("Bot poll:\n"+str(str(option_handler(1)+str(option_handler(2)+str(option_handler(3)+str(option_handler(4)+str(option_handler(5)+str(option_handler(6)+str(option_handler(7)+str(option_handler(8)+str(option_handler(9)+str(option_handler(10)))))))))))))### send poll options on each line, ugly so might redo later
    
    option_list = [option_1, option_2, option_3, option_4, option_5, option_6, option_7, option_8,option_9, option_10]
    global number_of_options_xrd
    global emoji_count
    emoji_count=0
    toggle=0
    number_of_options = 0
    for i in option_list:
        if i != "":
            number_of_options += 1
                
    number_of_options_xrd =    number_of_options
@bot.listen()
async def on_message(message):
    global number_of_options_xrd
    if message.author == bot.user:
        await asyncio.sleep(1)
        if "Bot poll:" in message.content:#highly unelegant reacton adder, might redo in the future
            if number_of_options_xrd != -1:
                if number_of_options_xrd == 1:
                    await message.add_reaction(number_emotes[number_of_options_xrd-1])
                if number_of_options_xrd == 2:
                    await message.add_reaction(number_emotes[number_of_options_xrd-2])
                    await message.add_reaction(number_emotes[number_of_options_xrd-1])
                if number_of_options_xrd == 3:
                    await message.add_reaction(number_emotes[number_of_options_xrd-3])
                    await message.add_reaction(number_emotes[number_of_options_xrd-2])
                    await message.add_reaction(number_emotes[number_of_options_xrd-1])
                if number_of_options_xrd == 4:
                    await message.add_reaction(number_emotes[number_of_options_xrd-4])
                    await message.add_reaction(number_emotes[number_of_options_xrd-3])
                    await message.add_reaction(number_emotes[number_of_options_xrd-2])
                    await message.add_reaction(number_emotes[number_of_options_xrd-1])
                if number_of_options_xrd == 6:
                    await message.add_reaction(number_emotes[number_of_options_xrd-5])
                    await message.add_reaction(number_emotes[number_of_options_xrd-4])
                    await message.add_reaction(number_emotes[number_of_options_xrd-3])
                    await message.add_reaction(number_emotes[number_of_options_xrd-2])
                    await message.add_reaction(number_emotes[number_of_options_xrd-1])
                if number_of_options_xrd == 6:
                    await message.add_reaction(number_emotes[number_of_options_xrd-6])
                    await message.add_reaction(number_emotes[number_of_options_xrd-5])
                    await message.add_reaction(number_emotes[number_of_options_xrd-4])
                    await message.add_reaction(number_emotes[number_of_options_xrd-3])
                    await message.add_reaction(number_emotes[number_of_options_xrd-2])
                    await message.add_reaction(number_emotes[number_of_options_xrd-1])
                if number_of_options_xrd == 7:
                    await message.add_reaction(number_emotes[number_of_options_xrd-7])
                    await message.add_reaction(number_emotes[number_of_options_xrd-6])
                    await message.add_reaction(number_emotes[number_of_options_xrd-5])
                    await message.add_reaction(number_emotes[number_of_options_xrd-4])
                    await message.add_reaction(number_emotes[number_of_options_xrd-3])
                    await message.add_reaction(number_emotes[number_of_options_xrd-2])
                    await message.add_reaction(number_emotes[number_of_options_xrd-1])
                if number_of_options_xrd == 8:
                    await message.add_reaction(number_emotes[number_of_options_xrd-8])
                    await message.add_reaction(number_emotes[number_of_options_xrd-7])
                    await message.add_reaction(number_emotes[number_of_options_xrd-6])
                    await message.add_reaction(number_emotes[number_of_options_xrd-5])
                    await message.add_reaction(number_emotes[number_of_options_xrd-4])
                    await message.add_reaction(number_emotes[number_of_options_xrd-3])
                    await message.add_reaction(number_emotes[number_of_options_xrd-2])
                    await message.add_reaction(number_emotes[number_of_options_xrd-1])
                if number_of_options_xrd == 9:
                    await message.add_reaction(number_emotes[number_of_options_xrd-9])
                    await message.add_reaction(number_emotes[number_of_options_xrd-8])
                    await message.add_reaction(number_emotes[number_of_options_xrd-7])
                    await message.add_reaction(number_emotes[number_of_options_xrd-6])
                    await message.add_reaction(number_emotes[number_of_options_xrd-5])
                    await message.add_reaction(number_emotes[number_of_options_xrd-4])
                    await message.add_reaction(number_emotes[number_of_options_xrd-3])
                    await message.add_reaction(number_emotes[number_of_options_xrd-2])
                    await message.add_reaction(number_emotes[number_of_options_xrd-1])
                if number_of_options_xrd == 10:
                    await message.add_reaction(number_emotes[number_of_options_xrd-10])
                    await message.add_reaction(number_emotes[number_of_options_xrd-9])
                    await message.add_reaction(number_emotes[number_of_options_xrd-8])
                    await message.add_reaction(number_emotes[number_of_options_xrd-7])
                    await message.add_reaction(number_emotes[number_of_options_xrd-6])
                    await message.add_reaction(number_emotes[number_of_options_xrd-5])
                    await message.add_reaction(number_emotes[number_of_options_xrd-4])
                    await message.add_reaction(number_emotes[number_of_options_xrd-3])
                    await message.add_reaction(number_emotes[number_of_options_xrd-2])
                    await message.add_reaction(number_emotes[number_of_options_xrd-1])
    await asyncio.sleep(1)
bot.run(discord_token)
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

