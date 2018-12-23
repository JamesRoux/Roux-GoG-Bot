import discord
from pprint import pprint
import json

#
# This is where I will import the modules for each dataset as they're made
#
import modules.research
from modules.research import get_data

with open('keys.json') as keys:
    keys = json.load(keys)
    TOKEN = keys["bot_token"]

client = discord.Client()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!roux'):
        command = message.content[6:]
        msg = get_data(command)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

client.run(TOKEN)
