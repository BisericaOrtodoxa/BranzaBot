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

from jikanpy import Jikan  # jikanpy_v4

jikan = Jikan()
qcf = "<:236:1074633458275602455>"
qcb = "<:214:1074633166670807141>"
dp_regular = "<:dp:1074634272775884811>"
dp_reversed = "<:421:1074634289427251310>"
half_circle_forward = "<:41236:1074633617034194965>"
half_circle_back = "<:63214:1074633787297779824>"
six_emoji = "<:6_:1074634127061553193>"
one_emoji = ""
three_emoji = ""
four_emoji = "<:4_:1074634110301130802>"
five_emoji = ""
six_emoji = ""
seven_emoji = ""
eight_emoji = ""
nine_emoji = ""




#########
game_squares = {"square_1": 0, "square_2": 0, "square_3": 0, "square_4": 0, "square_5": 0, "square_6": 0, "square_7": 0,
                "square_8": 0, "square_9": 0}
square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
site = " wikipedia.org"
discord_token = "MTAxOTY1NjYxNjkyMjA2MjkyOA.GOmKyd.zOPnMIezuC6_A-bQq3dAhB1TEFPFlIDSOBv780"
intents = discord.Intents.all()
intents.message_content = True
bot = discord.Bot(intents=intents)
number_emotes = ("1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟")
number_of_options_xrd = -1


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


@bot.slash_command(name="seconds", description="Set a timer in seconds")  # this decorator makes a slash command
@option("seconds", description="Number of seconds")
async def timer(ctx, seconds: int):
    print("A timer was set. Duration: " + str(seconds) + " seconds")
    await ctx.respond("Timer set to " + str(seconds) + " seconds")
    await asyncio.sleep(seconds)
    await ctx.respond("Time has passed")


# my implementation of a timer command(in seconds). I could make it so it takes days and hours but I'm too lazy

##########################
@bot.slash_command(name="b64_e", description="Encodes a string using base64")  # base64 encode command
@option("string")
async def b64_e(ctx, string: str):
    async with ctx.typing():
        string_to_ascii = string.encode("utf8")
        base64_to_ascii = base64.b64encode(string_to_ascii)
        base64_string = base64_to_ascii.decode("utf8")
        await ctx.respond(base64_string)


#####################################
def motion_replacer(msg_content):
    msg_content_v2 = ""
    one_emoji = ""
    three_emoji = ""
    four_emoji = "<:4_:1074634110301130802>"
    five_emoji = ""
    six_emoji = "<:6_:1074634127061553193>"
    seven_emoji = ""
    eight_emoji = "<:8_:1074634053174693918>"
    nine_emoji = ""
    p_emoji="<:p_:1074647629864128654>"
    k_emoji="<:k_:1074647586750877736>"
    s_emoji="<:s_:1074647569172529233>"
    hs_emoji="<:hs:1074647555801100288>"
    d_emoji="<:d_:1074647542219948112>"
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
        discord_message_3 =discord_message_2.replace("HS",hs_emoji)
        if "D_" in discord_message:
            discord_message_4 =discord_message_3
        else:     
            discord_message_4 =discord_message_3.replace("D",d_emoji)
        if "S_" in discord_message:    
            discord_message_5 =discord_message_4
        else:
            discord_message_5 =discord_message_4.replace("S",s_emoji)
        return discord_message_5
    if ":236:" in msg_content:
        pass
    elif ":421:" in msg_content:
        pass
    elif ":623:" in msg_content:
        pass
    elif ":63214:" in msg_content:
        pass
    elif ":41236:" in msg_content:
        pass
    elif ":214:" in msg_content:
        pass
    else:
        if "236236" in msg_content:
            msg_content_v2 = msg_content.replace("236236", "<:236:1074633458275602455><:236:1074633458275602455>")
            msg_content_v2 = attack_replacer(msg_content_v2)
            if "214236236" in msg_content:
                msg_content_v2 = msg_content.replace("214236236", "<:214:1074633166670807141><:236:1074633458275602455><:236:1074633458275602455>")    
            if "214214" in msg_content:
                msg_content_v2 = msg_content.replace("214214", "<:214:1074633166670807141><:214:1074633166670807141>")
            
                if "41236" in msg_content:
                    msg_content_v2 = msg_content.replace("41236", "<:41236:1074633617034194965>")
                    
                    if "63214" in msg_content:
                        msg_content_v2 = msg_content_v2.replace("63214", "<:63214:1074633787297779824>")
                        
                        if "623" in msg_content:
                            msg_content_v2 = msg_content_v2.replace("623", "<:dp:1074634272775884811>")
                            
                            if "421" in msg_content:
                                msg_content_v2 = msg_content_v2.replace("421", "<:421:1074634289427251310>")
                                
                                if "236" in msg_content:
                                    msg_content_v2 = msg_content_v2.replace("236", "<:236:1074633458275602455>")
                                    
                                    if "214" in msg_content:
                                        msg_content_v2 = msg_content_v2.replace("214", "<:214:1074633166670807141>")
                                        
                                        if "2P" or "2K" or "2S" or "2HS" or "2D" in msg_content:
                                            msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>")
                                            msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>")
                                            msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>")
                                            msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>")
                                            msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>")
                                            
                                            
        elif "41236" in msg_content:
            msg_content_v2 = msg_content.replace("41236", "<:41236:1074633617034194965>")
            msg_content_v2 = attack_replacer(msg_content_v2)
            if "63214" in msg_content:
                msg_content_v2 = msg_content_v2.replace("63214", "<:63214:1074633787297779824>")

                if "623" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("623", "<:dp:1074634272775884811>")
           
                    if "421" in msg_content:
                        msg_content_v2 = msg_content_v2.replace("421", "<:421:1074634289427251310>")
                
                        if "236" in msg_content:
                            msg_content_v2 = msg_content_v2.replace("236", "<:236:1074633458275602455>")
                     
                            if "214" in msg_content:
                                msg_content_v2 = msg_content_v2.replace("214", "<:214:1074633166670807141>")
                 
                                if "2" in msg_content:
                                    msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>")
                                    msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>")
                                    msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>")
                                    msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>")
                                    msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>")
                       
                                if "6" in msg_content:
                                    msg_content_v2 = msg_content_v2.replace("6P", six_emoji)
                                    msg_content_v2 = msg_content_v2.replace("6K", six_emoji)
                                    msg_content_v2 = msg_content_v2.replace("6S", six_emoji)
                                    msg_content_v2 = msg_content_v2.replace("6HS", six_emoji)
                                    msg_content_v2 = msg_content_v2.replace("6D", six_emoji)
                              
            else:
                if "2" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>")
                    msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>")
                    msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>")
                    msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>")
                    msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>")
                  
                if "6" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("6P", "<:6_:1074634127061553193>" )
                    msg_content_v2 = msg_content_v2.replace("6K", "<:6_:1074634127061553193>")
                    msg_content_v2 = msg_content_v2.replace("6S", "<:6_:1074634127061553193>")
                    msg_content_v2 = msg_content_v2.replace("6HS", "<:6_:1074634127061553193>")
                    msg_content_v2 = msg_content_v2.replace("6D", "<:6_:1074634127061553193>")
                    msg_content_v2 = attack_replacer(msg_content_v2)

        elif "63214" in msg_content:
            msg_content_v2 = msg_content.replace("63214", "<:63214:1074633787297779824>")
            msg_content_v2 = attack_replacer(msg_content_v2)
            if "623" in msg_content:
                msg_content_v2 = msg_content_v2.replace("623", "<:dp:1074634272775884811>")
                if "421" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("421", "<:421:1074634289427251310>")
                   
                    if "236" in msg_content:
                        msg_content_v2 = msg_content_v2.replace("236", "<:236:1074633458275602455>")
                      
                        if "214" in msg_content:
                            msg_content_v2 = msg_content_v2.replace("214", "<:214:1074633166670807141>")
                            
                        if "236" in msg_content:
                            msg_content_v2 = msg_content_v2.replace("236", "<:236:1074633458275602455>")
                            
                            if "2" in msg_content:
                                msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>")
                                msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>")
                                msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>")
                                msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>")
                                msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>")
                                
                            if "6" in msg_content:
                                msg_content_v2 = msg_content_v2.replace("6P", six_emoji)
                                msg_content_v2 = msg_content_v2.replace("6K", six_emoji)
                                msg_content_v2 = msg_content_v2.replace("6S", six_emoji)
                                msg_content_v2 = msg_content_v2.replace("6HS", six_emoji)
                                msg_content_v2 = msg_content_v2.replace("6D", six_emoji)
                                
                    else:
                        if "2" in msg_content:
                            msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>")
                            msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>")
                            msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>")
                            msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>")
                            msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>")
                           
                        if "6" in msg_content:
                            msg_content_v2 = msg_content_v2.replace("6P", "<:6_:1074634127061553193>")
                            msg_content_v2 = msg_content_v2.replace("6K", "<:6_:1074634127061553193>")
                            msg_content_v2 = msg_content_v2.replace("6S", "<:6_:1074634127061553193>")
                            msg_content_v2 = msg_content_v2.replace("6HS", "<:6_:1074634127061553193>")
                            msg_content_v2 = msg_content_v2.replace("6D", "<:6_:1074634127061553193>")
                            
                else:
                    if "2" in msg_content:
                        msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>" + p_emoji)
                        msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>K")
                        msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>S")
                        msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>HS")
                        msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>D")
                        msg_content_v2 = attack_replacer(msg_content_v2)
                    if "6" in msg_content:
                        msg_content_v2 = msg_content_v2.replace("6P", "<:6_:1074634127061553193>" + p_emoji)
                        msg_content_v2 = msg_content_v2.replace("6K", "<:6_:1074634127061553193>" + "K")
                        msg_content_v2 = msg_content_v2.replace("6S", "<:6_:1074634127061553193>" + "S")
                        msg_content_v2 = msg_content_v2.replace("6HS", "<:6_:1074634127061553193>" + "HS")
                        msg_content_v2 = msg_content_v2.replace("6D", "<:6_:1074634127061553193>" + "D")
                        msg_content_v2 = attack_replacer(msg_content_v2)
            else:
                if "2" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>")
                    msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>")
                    msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>")
                    msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>")
                    msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>")
                    
                if "6" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("6P", "<:6_:1074634127061553193>")
                    msg_content_v2 = msg_content_v2.replace("6K", "<:6_:1074634127061553193>")
                    msg_content_v2 = msg_content_v2.replace("6S", "<:6_:1074634127061553193>")
                    msg_content_v2 = msg_content_v2.replace("6HS", "<:6_:1074634127061553193>")
                    msg_content_v2 = msg_content_v2.replace("6D", "<:6_:1074634127061553193>")
                    


        elif "623" in msg_content:
            msg_content_v2 = msg_content.replace("623", "<:dp:1074634272775884811>")
            msg_content_v2 = attack_replacer(msg_content_v2)
            print("?????????????????????"+msg_content_v2)
            if "421" in msg_content:
                msg_content_v2 = msg_content_v2.replace("421", "<:421:1074634289427251310>")

                if "214" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("214", "<:214:1074633166670807141>")

                    if "236" in msg_content:
                        msg_content_v2 = msg_content_v2.replace("236", "<:236:1074633458275602455>")

                        if "2" in msg_content:
                            msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>")
                            msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>")
                            msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>")
                            msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>")
                            msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>")

                        if "6" in msg_content:
                            msg_content_v2 = msg_content_v2.replace("6P", "<:6_:1074634127061553193>")
                            msg_content_v2 = msg_content_v2.replace("6K", "<:6_:1074634127061553193>")
                            msg_content_v2 = msg_content_v2.replace("6S", "<:6_:1074634127061553193>")
                            msg_content_v2 = msg_content_v2.replace("6HS", "<:6_:1074634127061553193>")
                            msg_content_v2 = msg_content_v2.replace("6D", "<:6_:1074634127061553193>")

                    else:
                        if "2" in msg_content:
                            msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>")
                            msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>")
                            msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>")
                            msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>")
                            msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>")

                        if "6" in msg_content:
                            msg_content_v2 = msg_content_v2.replace("6P", "<:6_:1074634127061553193>")
                            msg_content_v2 = msg_content_v2.replace("6K", six_emoji)
                            msg_content_v2 = msg_content_v2.replace("6S", six_emoji)
                            msg_content_v2 = msg_content_v2.replace("6HS", six_emoji)
                            msg_content_v2 = msg_content_v2.replace("6D", six_emoji)

                else:
                    if "2" in msg_content:
                        msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>")
                        msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>")
                        msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>")
                        msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>")
                        msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>")
                       
                    if "6" in msg_content:
                        msg_content_v2 = msg_content_v2.replace("6P", six_emoji)
                        msg_content_v2 = msg_content_v2.replace("6K", six_emoji)
                        msg_content_v2 = msg_content_v2.replace("6S", six_emoji)
                        msg_content_v2 = msg_content_v2.replace("6HS", six_emoji)
                        msg_content_v2 = msg_content_v2.replace("6D", six_emoji)

            else:
                if "2" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>"+p_emoji)
                    msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>K")
                    msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>S")
                    msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>HS")
                    msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>D")
                    msg_content_v2 = attack_replacer(msg_content_v2)
                if "6" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("6P", six_emoji)
                    msg_content_v2 = msg_content_v2.replace("6K", six_emoji)
                    msg_content_v2 = msg_content_v2.replace("6S", six_emoji)
                    msg_content_v2 = msg_content_v2.replace("6HS", six_emoji)
                    msg_content_v2 = msg_content_v2.replace("6D", six_emoji)

            if "214" in msg_content:
                msg_content_v2 = msg_content_v2.replace("214", "<:214:1074633166670807141>")
                if "2P" or "2K" or "2S" or "2HS" or "2D" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>"+p_emoji)
                    msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>K")
                    msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>S")
                    msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>HS")
                    msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>D")
                    msg_content_v2 = attack_replacer(msg_content_v2)
                if "6" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("6P", six_emoji + p_emoji)
                    msg_content_v2 = msg_content_v2.replace("6K", six_emoji + "K")
                    msg_content_v2 = msg_content_v2.replace("6S", six_emoji + "S")
                    msg_content_v2 = msg_content_v2.replace("6HS", six_emoji + "HS")
                    msg_content_v2 = msg_content_v2.replace("6D", six_emoji + "D")
                    msg_content_v2 = attack_replacer(msg_content_v2)
            if "236" in msg_content:
                msg_content_v2 = msg_content_v2.replace("236", "<:236:1074633458275602455>")
                if "2" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>"+p_emoji)
                    msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>K")
                    msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>S")
                    msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>HS")
                    msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>D")
                    msg_content_v2 = attack_replacer(msg_content_v2)
                if "6" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("6P<:2_:1074634029422346260>", six_emoji)
                    msg_content_v2 = msg_content_v2.replace("6K", six_emoji)
                    msg_content_v2 = msg_content_v2.replace("6S", six_emoji)
                    msg_content_v2 = msg_content_v2.replace("6HS", six_emoji)
                    msg_content_v2 = msg_content_v2.replace("6D", six_emoji)
                    msg_content_v2 = attack_replacer(msg_content_v2)
            else:
                if "2" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>"+p_emoji)
                    msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>K")
                    msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>S")
                    msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>HS")
                    msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>D")
       
                if "6" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("6P", six_emoji + p_emoji)
                    msg_content_v2 = msg_content_v2.replace("6K", six_emoji + "K")
                    msg_content_v2 = msg_content_v2.replace("6S", six_emoji + "S")
                    msg_content_v2 = msg_content_v2.replace("6HS", six_emoji + "HS")
                    msg_content_v2 = msg_content_v2.replace("6D", six_emoji + "D")
 
        elif "421" in msg_content:
            msg_content_v2 = msg_content.replace("421", "<:421:1074634289427251310>")
            msg_content_v2 = attack_replacer(msg_content_v2)
            if "236" in msg_content:
                msg_content_v2 = msg_content_v2.replace("236", "<:236:1074633458275602455>")
                msg_content_v2 = attack_replacer(msg_content_v2)
                if "214" in msg_content:
                    msg_content_v2 = msg_content_v2.replace("214", "<:214:1074633166670807141>")
                    if "2P" or "2K" or "2S" or "2HS" or "2D" in msg_content:
                        msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>"+p_emoji)
                        msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>K")
                        msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>S")
                        msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>HS")
                        msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>D")
                        msg_content_v2 = attack_replacer(msg_content_v2)
                    if "6" in msg_content:
                        msg_content_v2 = msg_content_v2.replace("6P", six_emoji + p_emoji)
                        msg_content_v2 = msg_content_v2.replace("6K", six_emoji + "K")
                        msg_content_v2 = msg_content_v2.replace("6S", six_emoji + "S")
                        msg_content_v2 = msg_content_v2.replace("6HS", six_emoji + "HS")
                        msg_content_v2 = msg_content_v2.replace("6D", six_emoji + "D")
                        msg_content_v2 = attack_replacer(msg_content_v2)
        elif "236" in msg_content:
            msg_content_v2 = attack_replacer(msg_content)
            msg_content_v2 = msg_content_v2.replace("236", "<:236:1074633458275602455>")
            if "214" in msg_content:
                msg_content_v2 = msg_content_v2.replace("214", "<:214:1074633166670807141>")
            if "2" in msg_content_v2:
                print("|||||||||||||||||||||"+ msg_content)
                msg_content_v2 = msg_content_v2.replace("2P<", "<:2_:1074634029422346260>")
                msg_content_v2 = msg_content_v2.replace("2K<", "<:2_:1074634029422346260>")
                msg_content_v2 = msg_content_v2.replace("2S<", "<:2_:1074634029422346260>")
                msg_content_v2 = msg_content_v2.replace("2HS<", "<:2_:1074634029422346260>")
                msg_content_v2 = msg_content_v2.replace("2D<", "<:2_:1074634029422346260>")
                
            if "6" in msg_content:
                msg_content_v2 = msg_content_v2.replace("6<", six_emoji+"<")
                msg_content_v2 = msg_content_v2.replace("6K<", six_emoji+"<")
                msg_content_v2 = msg_content_v2.replace("6S<", six_emoji+"<")
                msg_content_v2 = msg_content_v2.replace("6HS<", six_emoji+"<")
                msg_content_v2 = msg_content_v2.replace("6D<", six_emoji+"<")
                 

        elif "214" in msg_content:
            msg_content_v2 = msg_content.replace("214", "<:214:1074633166670807141>")
            msg_content_v2 = attack_replacer(msg_content_v2)
            if "2" in msg_content:
                msg_content_v2 = msg_content_v2.replace("2P", "<:2_:1074634029422346260>")
                msg_content_v2 = msg_content_v2.replace("2K", "<:2_:1074634029422346260>")
                msg_content_v2 = msg_content_v2.replace("2S", "<:2_:1074634029422346260>")
                msg_content_v2 = msg_content_v2.replace("2HS", "<:2_:1074634029422346260>")
                msg_content_v2 = msg_content_v2.replace("2D", "<:2_:1074634029422346260>")

            if "6" in msg_content:
                msg_content_v2 = msg_content_v2.replace("6P", six_emoji)
                msg_content_v2 = msg_content_v2.replace("6K", six_emoji)
                msg_content_v2 = msg_content_v2.replace("6S", six_emoji)
                msg_content_v2 = msg_content_v2.replace("6HS", six_emoji)
                msg_content_v2 = msg_content_v2.replace("6D", six_emoji)

        if msg_content != msg_content_v2:
            return str(msg_content_v2)
        if msg_content == msg_content_v2:
            return ""


######################
# if "sus" in message.content:
# await message.reply('Among SUS', mention_author=False)

####################################
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
            game_squares["square_3"]) + "\n" + number_to_emoji(game_squares["square_4"]) + number_to_emoji(
            game_squares["square_5"]) + number_to_emoji(game_squares["square_6"]) + "\n" + number_to_emoji(
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
    print(f'We have logged in as {bot.user}' + " Running on: " + str(platform.platform()))


###################################### message logging. logs:messages sent, deleted and edited and stores them into msg_logs.txt. Upon request via slash command, this file is uploaded to discord
@bot.slash_command(name="logs", description="Fetch the logs from the stored file(the bot messages are also stored)",
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


@bot.listen()
async def on_message(message):
    logs = open("msg_logs.txt", "a")
    logs.write("\n" + str(message.author) + "(" + str(message.created_at) + ")" + ": " + str(
        message.content) + "   channel: " + str(message.channel.mention))
    print("The following message was logged: " + str(message.content) + " |written by " + str(
        message.author) + " channel: " + str(message.channel.mention))
    logs.close
    print("Logs file size: " + str(os.path.getsize("msg_logs.txt")))
    if int(os.path.getsize("msg_logs.txt")) > 8_000_000:
        logs = open("msg_logs.txt", "r")
        await message.channel.send("Logs file size limit exceeded(8mb)), sending logs then deleting server copy")
        await message.channel.send(file=discord.File('msg_logs.txt'))
        os.remove("demofile.txt")
        logs.close
        ###################### motion input transformer corner
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
async def poll(ctx, option_1: str, option_2: str, option_3: str, option_4: str, option_5: str, option_6: str,
               option_7: str, option_8: str, option_9: str, option_10: str):
    number_emotes = ("1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟")

    def option_handler(x):
        option_list = [option_1, option_2, option_3, option_4, option_5, option_6, option_7, option_8, option_9,
                       option_10]
        if option_list[x - 1] != "":
            return str(option_list[x - 1] + '\n\n')

        if option_list[x - 1] == "":
            return ("")

    await ctx.respond("Bot poll:\n" + str(str(option_handler(1) + str(option_handler(2) + str(option_handler(3) + str(
        option_handler(4) + str(option_handler(5) + str(option_handler(6) + str(option_handler(7) + str(
            option_handler(8) + str(option_handler(9) + str(
                option_handler(10)))))))))))))  ### send poll options on each line, ugly so might redo later

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
        if "Bot poll:" in message.content:  # highly unelegant reacton adder, might redo in the future
            if number_of_options_xrd != -1:
                if number_of_options_xrd == 1:
                    await message.add_reaction(number_emotes[number_of_options_xrd - 1])
                if number_of_options_xrd == 2:
                    await message.add_reaction(number_emotes[number_of_options_xrd - 2])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 1])
                if number_of_options_xrd == 3:
                    await message.add_reaction(number_emotes[number_of_options_xrd - 3])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 2])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 1])
                if number_of_options_xrd == 4:
                    await message.add_reaction(number_emotes[number_of_options_xrd - 4])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 3])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 2])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 1])
                if number_of_options_xrd == 6:
                    await message.add_reaction(number_emotes[number_of_options_xrd - 5])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 4])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 3])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 2])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 1])
                if number_of_options_xrd == 6:
                    await message.add_reaction(number_emotes[number_of_options_xrd - 6])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 5])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 4])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 3])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 2])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 1])
                if number_of_options_xrd == 7:
                    await message.add_reaction(number_emotes[number_of_options_xrd - 7])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 6])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 5])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 4])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 3])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 2])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 1])
                if number_of_options_xrd == 8:
                    await message.add_reaction(number_emotes[number_of_options_xrd - 8])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 7])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 6])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 5])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 4])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 3])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 2])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 1])
                if number_of_options_xrd == 9:
                    await message.add_reaction(number_emotes[number_of_options_xrd - 9])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 8])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 7])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 6])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 5])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 4])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 3])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 2])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 1])
                if number_of_options_xrd == 10:
                    await message.add_reaction(number_emotes[number_of_options_xrd - 10])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 9])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 8])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 7])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 6])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 5])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 4])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 3])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 2])
                    await message.add_reaction(number_emotes[number_of_options_xrd - 1])
    await asyncio.sleep(1)


###################################### search for anime and manga(can't do much more since the api appears to not have more)

@bot.slash_command(name="anime_search", description="Search for anime")
@option("anime_name")
@bot.event
async def anime_search(ctx, anime_name: str):
    search = jikan.search('anime', anime_name, page=1, parameters={"limit": "1"})
    # print(search["data"][0]["url"])
    await ctx.respond(str(search["data"][0]["url"]))


##########
@bot.slash_command(name="anime_character_search", description="Search for anime character",
                   guild_ids=[1042811421718761606])
@option("character_name")
@bot.event
async def anime_character_search(ctx, character_name: str):
    search = jikan.search('characters', character_name, page=1, parameters={"limit": "1"})
    # print(search["data"][0]["url"])
    await ctx.respond(str(search["data"][0]["url"]))


##########
@bot.slash_command(name="manga_search", description="Search for manga")
@option("manga_name")
@bot.event
async def manga_search(ctx, manga_name: str):
    search = jikan.search('manga', manga_name, page=1, parameters={"limit": "1"})
    # print(search["data"][0]["url"])
    await ctx.respond(str(search["data"][0]["url"]))


##########
@bot.slash_command(name="servers", description="Lists the servers that the bot is on", guild_ids=[1042811421718761606])
@option("invite", required=False, default='')
@bot.event
async def servers(ctx, invite: str):
    activeservers = bot.guilds
    for guild in activeservers:
        if invite == "sure":
            discord_guild = bot.get_guild(int(guild.id))
            link = await discord_guild.text_channels[0].create_invite()
            await ctx.respond(
                "Server name:" + str(guild.name) + "\n Guild id:" + str(guild.id) + "\n invite: " + str(link))
        else:
            await ctx.respond("Server name:" + str(guild.name) + "\n Guild id:" + str(guild.id))


bot.run(discord_token)
