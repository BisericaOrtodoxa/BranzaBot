import discord
from googlesearch import search
import os

discord_token=input("bot token:")
#def cauta(quer):
#for j in search(quer, num=1):
#result=j

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
    if message.content.startswith('$branza'):
        query = message.content
        query_2 = query.replace("$branza", "") + " wikipedia.org"
        for j in search(query_2, num=1):
            await message.channel.send(j)


client.run(discord_token)
