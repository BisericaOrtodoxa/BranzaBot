import discord
from googlesearch import search
import os
import random

discord_token=input("bot token:")
comanda="$branza"

def rm_command(x): #prelucrare mesaj și excludere comanda
    query = message.content
    query_2 = query.replace(x, "") + " wikipedia.org"
    

intents = discord.Intents.default()
intents.message_content = True

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
        rm_command(comanda)
        for j in search(query_2, num=1, stop=1):
            await message.channel.send(j)

client.run(discord_token)
