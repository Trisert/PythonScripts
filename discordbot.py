#!/usr/bin/env python3

import discord

client = discord.Client()

vanuzzo = ['Vanuzzo', 'VANUZZO', 'vanuzzo']

@client.event
async def on_ready():
    print('We have logged in as  {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Vanuzzo'):
        await message.channel.send('Merda')

    if message.content.startswith('vanuzzo'):
        await message.channel.send('Merda')

    if message.content.startswith('VANUZZO'):
        await message.channel.send('Merda')

    if message.content.startswith("Leonardo"):
        await message.channel.send("No vabbè fra swishami un blunt a swishland")

    if message.content.startswith("Come direbbe il sommo"):
        await message.channel.send("V A F F A N C U L O")

client.run('NzczNTUxOTU3MzQ0Mzg3MTIy.X6K4Zg.ktbamlYF-A1nwAlt81NMn3IXvkg')
