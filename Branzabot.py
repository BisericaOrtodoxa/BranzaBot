import discord
from googlesearch import search
from discord import option
import asyncio
import time
import base64
# import youtube_dl
import os
from datetime import datetime
from discord.ext import commands
import platform
from jikanpy import Jikan  # must be jikanpy_v4!

jikan = Jikan()
############ fighting game input emojis
qcf = "<:236:1074633458275602455>"
qcb_emoji = "<:qcb:1074633166670807141>"
dp_regular = "<:dp:1074634272775884811>"
dp_reversed = "<:421:1074634289427251310>"
half_circle_forward = "<:41236:1074633617034194965>"
half_circle_back = "<:f_cb:1074633787297779824>"
#########
game_squares = {"square_1": 0, "square_2": 0, "square_3": 0, "square_4": 0, "square_5": 0, "square_6": 0, "square_7": 0, "square_8": 0, "square_9": 0}
square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
site = " wikipedia.org"
discord_token = "just a stranger in a bus"
intents = discord.Intents.all()
intents.message_content = True
bot = discord.Bot(intents=intents)
number_emotes = ("1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟")
number_of_options_xrd = -1

##########################
@bot.slash_command(name="google", description="Searches a website for the desired info", guild_ids=[1042811421718761606])  # this decorator makes a slash command
@option("website", description="Enter website", required=False, default='')
@option("term", description="")


async def google(ctx, term, website: str):  # command that performs a Google search based on user input via slash command
    async with ctx.typing():
        for j in search(str(term) + " " + str(website), num=1, stop=1):
            await ctx.respond(j)
###################################### my implementation of a timer command(in seconds). I could make it so it takes days and hours but I'm too lazy
@bot.slash_command(name="seconds", description="Set a timer in seconds")  # this decorator makes a slash command
@option("seconds", description="Number of seconds")
async def timer(ctx, seconds: int):
    print("A timer was set. Duration: " + str(seconds) + " seconds")
    await ctx.respond("Timer set to " + str(seconds) + " seconds")
    await asyncio.sleep(seconds)
    await ctx.respond("Time has passed")

########################## base64 encode and decode commands
@bot.slash_command(name="b64_e", description="Encodes a string using base64")  
@option("string")
async def b64_e(ctx, string: str):
    async with ctx.typing():
        string_to_ascii = string.encode("utf8")
        base64_to_ascii = base64.b64encode(string_to_ascii)
        base64_string = base64_to_ascii.decode("utf8")
        await ctx.respond(base64_string)

@bot.slash_command(name="b64_d", description="Decode a string using base64")  
@option("string")
async def b64_d(ctx, string: str):
    async with ctx.typing():
        string_to_ascii = string.encode("ascii")
        base64_to_ascii = base64.b64decode(string_to_ascii)
        
        await ctx.respond( base64_to_ascii)
##################################### this replaces the numpad notation in a message with a visual indicator of the inputs and attacks
def motion_replacer(msg_content):
    msg_content_v2 = ""
    one_emoji = "<:1_:1077555101994057738>"
    two_emoji = "<:2_:1074634029422346260> "
    three_emoji = ""
    four_emoji = "<:4_:1074634110301130802>"
    five_emoji = "<:neutral:1075002232099045387> "
    six_emoji = "<:6_:1074634127061553193>"
    seven_emoji = ""
    eight_emoji = "<:8_:1074634053174693918>"
    nine_emoji = ""
    p_emoji="<:p_:1074647629864128654>"
    k_emoji="<:k_:1074647586750877736>"
    s_emoji="<:s_:1074647569172529233>"
    hs_emoji="<:hs:1074647555801100288>"
    d_emoji="<:d_:1074647542219948112>"
    
    dp_back_emoji= "<:dp_back:1074634289427251310>"
    qcb_emoji = "<:qcb:1074633166670807141>"
    qcf_emoji="<:qcf:1074633458275602455>"
    half_circle_back = "<:f_cb:1074633787297779824>"
    lets_hope_nobody_types_this= "<{[||ball$InYOm@m@j@ws"
    def attack_replacer(discord_message):
        discord_message_1=""
        discord_message_2=""
        discord_message_3=""
        discord_message_4=""
        discord_message_5=""
        if "P_" in discord_message:
             discord_message_1 =discord_message
        else:        
            discord_message_1 =discord_message.replace("P",p_emoji)
        if "K_" in discord_message:
            discord_message_2 =discord_message_1
        else:    
            discord_message_2 =discord_message_1.replace("K",k_emoji)
        discord_message_3 =discord_message_2.replace("CH",lets_hope_nobody_types_this)
        discord_message_3 =discord_message_3.replace("HS",hs_emoji)
        discord_message_3 =discord_message_3.replace("H",hs_emoji)
        discord_message_3 =discord_message_3.replace(lets_hope_nobody_types_this,"CH")
        if "D_" in discord_message:
            discord_message_4 =discord_message_3
        else:     
            discord_message_4 =discord_message_3.replace("D",d_emoji)
        if "S_" in discord_message:    
            discord_message_5 =discord_message_4
        else:
            discord_message_5 =discord_message_4.replace("WS",lets_hope_nobody_types_this)
            discord_message_5 =discord_message_5.replace("S",s_emoji)
            discord_message_5 =discord_message_5.replace(lets_hope_nobody_types_this,"WS")
        return discord_message_5     
    def singular_direction_replacer(x):
        def repeated_replacer(x,number,number_emoji):
            x = x.replace(" "+number, " "+number_emoji)
            x = x.replace(number+" ", number_emoji+" ")
            x = x.replace("("+number, " "+number_emoji)
            x = x.replace(number+")", number_emoji+")")            
            x = x.replace(number+"<", number_emoji+"<")
            x = x.replace(">"+number, ">"+number_emoji)
            x = x.replace(number+"<", number_emoji+"<")
            x = x.replace(">"+number, ">"+number_emoji)
            return x
        if "1" in x:       
            x = repeated_replacer(x,"1",one_emoji)         
        if "2" in x:       
            x = repeated_replacer(x,"2",two_emoji) 
        #if "3" in msg_content:       
        #   x = repeated_replacer(x,"3",_emoji)
        if "4" in x:  
            #print("BEFORE!!!!  "+ msg_content)
            x = repeated_replacer(x,"4",four_emoji)            
            #print("AFTER!!!!  "+ msg_content)
        if "5" in msg_content:
            x = repeated_replacer(x,"5",five_emoji)
         
        if "6" in x:       
            x = repeated_replacer(x,"6",six_emoji)
        #if "7" in msg_content:       
        #   x = repeated_replacer(x,"7",seven_emoji)
        if "8" in x:       
            x = repeated_replacer(x,"8",eight_emoji)
        #if "9" in msg_content:       
        #   x = repeated_replacer(x,"9",nine_emoji)
        return x    

    if ":623:" in msg_content:
        pass
    elif ":63214:" in msg_content:
        pass

    elif "<:" in msg_content:
        pass
    else:
        msg_content_v2 = ""
        if "236236" in msg_content:
            msg_content_v2 = msg_content.replace("236236", qcf_emoji+qcf_emoji)
            msg_content_v2 = attack_replacer(msg_content_v2)
            if "214236236" in msg_content:
                msg_content_v2 = msg_content.replace("214236236", qcb_emoji+qcf_emoji+qcf_emoji)   
                
        if "214214" in msg_content:
            if msg_content_v2 == "":
                msg_content_v2 = msg_content.replace("214214", qcb_emoji+qcb_emoji)
            else:
                msg_content_v2 = msg_content_v2.replace("214214", qcb_emoji+qcb_emoji)
                                            
        if "41236" in msg_content:
            if msg_content_v2 == "":
                msg_content_v2 = msg_content.replace("41236", "<:f_cf:1074633617034194965>")
            else:
                msg_content_v2 = msg_content_v2.replace("41236", "<:f_cf:1074633617034194965>")
          
        if "63214" in msg_content:
            if msg_content_v2 == "":
                msg_content_v2 = msg_content.replace("63214", half_circle_back)
            else:
                msg_content_v2 = msg_content_v2.replace("63214", half_circle_back)
            
        if "623" in msg_content:
            if msg_content_v2 == "":
                msg_content_v2 = msg_content.replace("623", "<:dp:1074634272775884811>")
            else:
                msg_content_v2 = msg_content_v2.replace("623", "<:dp:1074634272775884811>")                    
 
        if "421" in msg_content:
            if msg_content_v2 == "":
                msg_content_v2 = msg_content.replace("421", dp_back_emoji)
            else:
                msg_content_v2 = msg_content_v2.replace("421", dp_back_emoji)
      
        if "236" in msg_content:
            if msg_content_v2 == "":
                msg_content_v2 = msg_content.replace("236", qcf_emoji)
            else:
                msg_content_v2 = msg_content_v2.replace("236", qcf_emoji)

        if "214" in msg_content:
            if msg_content_v2 == "":
                msg_content_v2 = msg_content.replace("214", "<:214:1074633166670807141>")
            else:
                msg_content_v2 = msg_content_v2.replace("214", "<:214:1074633166670807141>")

        msg_content_v2 = singular_direction_replacer(msg_content_v2)
        msg_content_v2 = attack_replacer(msg_content_v2)
        if msg_content != msg_content_v2:
            return str(msg_content_v2)
        if msg_content == msg_content_v2:
            return ""


######################
# if "sus" in message.content:
# await message.reply('Among SUS', mention_author=False)

#####################################my x and o command, i wont bother to implement instances. so each game can be nteracted with by anyone
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
                return "❌"
            elif a == 2:
                return "⭕"
            else:
                return "◼️"

        def win_state(square_X_O):  # defines each winning state, im sure there was a better ay to do this but im not smart
            if game_squares["square_1"] == game_squares["square_2"] and game_squares["square_2"] == game_squares["square_3"] and game_squares["square_3"] == square_X_O:
                return "win"
            if game_squares["square_4"] == game_squares["square_5"] and game_squares["square_5"] == game_squares["square_6"] and game_squares["square_6"] == square_X_O:
                return "win"
            if game_squares["square_7"] == game_squares["square_8"] and game_squares["square_8"] == game_squares["square_9"] and game_squares["square_9"] == square_X_O:
                return "win"
            if game_squares["square_1"] == game_squares["square_5"] and game_squares["square_5"] == game_squares["square_9"] and game_squares["square_9"] == square_X_O:
                return "win"
            if game_squares["square_3"] == game_squares["square_5"] and game_squares["square_5"] == game_squares[ "square_7"] and game_squares["square_7"] == square_X_O:
                return "win"

        def square_changer(one_or_two):
            if reset == "yes":
                board_reset()
            if reset != "yes":    
                if square_number == 1:
                    game_squares["square_1"] = one_or_two

                elif square_number == 2:
                    game_squares["square_2"] = one_or_two

                elif square_number == 3:
                    game_squares["square_3"] = one_or_two

                elif square_number == 4:
                    game_squares["square_4"] = one_or_two

                elif square_number == 5:
                    game_squares["square_5"] = one_or_two

                elif square_number == 6:
                    game_squares["square_6"] = one_or_two

                elif square_number == 7:
                    game_squares["square_7"] = one_or_two

                elif square_number == 8:
                    game_squares["square_8"] = one_or_two

                elif square_number == 9:
                    game_squares["square_9"] = one_or_two

                else:
                    ctx.respond("Invalid square number")

        if x_or_o == "X" or x_or_o == "x":
            square_changer(1)
        if x_or_o == "O" or x_or_o == "o":
            square_changer(2)
    await ctx.respond(number_to_emoji(game_squares["square_1"]) + number_to_emoji(game_squares["square_2"]) + number_to_emoji(game_squares["square_3"]) + "\n" + number_to_emoji(game_squares["square_4"]) + number_to_emoji(game_squares["square_5"]) + number_to_emoji(game_squares["square_6"]) + "\n" + number_to_emoji(game_squares["square_7"]) + number_to_emoji(game_squares["square_8"]) + number_to_emoji(game_squares["square_9"]))  # send the state of the board after each move
    if win_state(1) == "win":  # checks if x won
        await ctx.channel.send("X won! Resetting board")
        board_reset()
    if win_state(2) == "win":  # checks if y won
        await ctx.channel.send("O won! Resetting board")
        board_reset()

#####################################
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}' + " Running on: " + str(platform.platform())) #message displayed on bot login, also displays info about the platform it is hosted on

###################################### message logging. logs:messages sent, deleted and edited and stores them into msg_logs.txt. Upon request via slash command, this file is uploaded to discord
@bot.slash_command(name="logs", description="Fetch the logs from the stored file(the bot messages are also stored)", guild_ids=[1042811421718761606])
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

@bot.listen()
async def on_message(message):
    logs = open("msg_logs.txt", "a")
    logs.write("\n" + str(message.author) + "(" + str(message.created_at) + ")" + ": " + str(message.content) + "   channel: " + str(message.channel.mention))
    print("The following message was logged: " + str(message.content) + " |written by " + str(message.author) + " channel: " + str(message.channel.mention))
    logs.close
    print("Logs file size: " + str(os.path.getsize("msg_logs.txt")))
    if int(os.path.getsize("msg_logs.txt")) > 8_000_000:
        logs = open("msg_logs.txt", "r")
        await message.channel.send("Logs file size limit exceeded(8mb)), sending logs then deleting server copy")
        #await message.channel.send(file=discord.File('msg_logs.txt'))    i dont want the logs to be sent automatically for now
        os.remove("demofile.txt")
        logs.close
        ###################### motion input transformer corner(the actual code is above) 
    if motion_replacer(message.content) != None and message.author != bot.user:
        if motion_replacer(message.content) != "":
            await message.reply(motion_replacer(message.content), mention_author=False)

###################################### this turns user input into a poll with added reaction emoij for voting reasons
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
async def poll(ctx, option_1: str, option_2: str, option_3: str, option_4: str, option_5: str, option_6: str,option_7: str, option_8: str, option_9: str, option_10: str):
    number_emotes = ("1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟")

    def option_handler(x):
        option_list = [option_1, option_2, option_3, option_4, option_5, option_6, option_7, option_8, option_9,option_10]
        if option_list[x - 1] != "":
            return str(option_list[x - 1] + '\n\n')
        
        if option_list[x - 1] == "":
            return ("")

    await ctx.respond("Bot poll:\n" + str(str(option_handler(1) + str(option_handler(2) + str(option_handler(3) + str(option_handler(4) + str(option_handler(5) + str(option_handler(6) + str(option_handler(7) + str(option_handler(8) + str(option_handler(9) + str(option_handler(10)))))))))))))  ### send poll options on each line, ugly so might redo later

    option_list = [option_1, option_2, option_3, option_4, option_5, option_6, option_7, option_8, option_9, option_10]
    global number_of_options_xrd
    global emoji_count
    emoji_count = 0
    toggle = 0
    number_of_options = 0
    for i in option_list:
        if i != "":
            number_of_options += 1

    number_of_options_xrd = number_of_options


@bot.listen()
async def on_message(message):
    global number_of_options_xrd
    if message.author == bot.user:
        await asyncio.sleep(1)
        if "Bot poll:" in message.content: 
            x =  number_of_options_xrd
            while x != 0:
                await message.add_reaction(number_emotes[number_of_options_xrd - x])
                x= x-1

    await asyncio.sleep(1)


###################################### search for anime and manga(can't do much more since the api appears to not have more)

@bot.slash_command(name="anime_search", description="Search for anime")
@option("anime_name")
@bot.event
async def anime_search(ctx, anime_name: str):
    search = jikan.search('anime', anime_name, page=1, parameters={"limit": "1"})
    # print(search["data"][0]["url"])
    await ctx.respond(str(search["data"][0]["url"]))


########## this searches user input on mal and returns the first link(anime character)
@bot.slash_command(name="anime_character_search", description="Search for anime character", guild_ids=[1042811421718761606])
@option("character_name")
@bot.event
async def anime_character_search(ctx, character_name: str):
    search = jikan.search('characters', character_name, page=1, parameters={"limit": "1"})
    # print(search["data"][0]["url"])
    await ctx.respond(str(search["data"][0]["url"]))


########## this searches user input on mal and returns the first link(manga)
@bot.slash_command(name="manga_search", description="Search for manga")
@option("manga_name")
@bot.event
async def manga_search(ctx, manga_name: str):
    search = jikan.search('manga', manga_name, page=1, parameters={"limit": "1"})
    # print(search["data"][0]["url"])
    await ctx.respond(str(search["data"][0]["url"]))


########## Lists the servers that the bot is on, if you write "sure" in the invite option, the bot will give you links to those servers too(if it has the permission to generate them)
@bot.slash_command(name="servers", description="Lists the servers that the bot is on", guild_ids=[1042811421718761606])
@option("invite", required=False, default='')
@bot.event
async def servers(ctx, invite: str):
    activeservers = bot.guilds
    for guild in activeservers:
        if invite == "sure":
            discord_guild = bot.get_guild(int(guild.id))
            link = await discord_guild.text_channels[0].create_invite()
            await ctx.respond("Server name:" + str(guild.name) + "\n Guild id:" + str(guild.id) + "\n invite: " + str(link))
        else:
            await ctx.respond("Server name:" + str(guild.name) + "\n Guild id:" + str(guild.id))


bot.run(discord_token)
