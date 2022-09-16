import discord
from googlesearch import search
import os
import random

discord_token=input("bot token:")
comanda="$branza"

intents = discord.Intents.default()
intents.message_content = True

def rm_command(x,mesaj): #prelucrare mesaj și excludere comanda  
    query = mesaj
    query_2 = query.replace(x, "") + " wikipedia.org"
    return query_2
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "porn" in message.content:
        await message.channel.send("nu-i voie")     
    if message.content.startswith(comanda):
        for j in search(rm_command(comanda,message.content), num=1, stop=1):
            await message.channel.send(j)

client.run(discord_token)
