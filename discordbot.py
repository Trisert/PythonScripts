#!/usr/bin/env python3

import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

"""
client = discord.Client()

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
"""
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def edoardo(ctx):
    await ctx.send('Merda')

@bot.command()
async def leonardo(ctx):
    await ctx.send('No vabbè fra swishami un blunt a swishland')

@bot.command()
async def v(ctx):
    await ctx.send('V A F F A N C U L O')

@bot.command()
async def nicola(ctx):
    await ctx.send('Vamavvo mavvone a Gambavave')

@bot.command()
async def ripeti(ctx, times: int, content):
    if times <= 20:
        if len(content) > 1:
            for i in range(times):
                await ctx.send(content)
    else:
        await ctx.send('Sparati coglione')

@bot.command()
async def dado(ctx, dado:str):
    try:
        rolls, limit = map(int, dado.split('d'))
    except Exception:
        await ctx.send('Sparati')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def decidi(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def pulisci(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)

bot.run('NzczNTUxOTU3MzQ0Mzg3MTIy.X6K4Zg.JyeWNIzLsyUCdyZrn0_KutVxJPk')
