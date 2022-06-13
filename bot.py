import asyncio
import os
import discord
from discord.ext import commands

#Alon R and Alon F

intents = discord.Intents.all()

client = commands.Bot(command_prefix = '>', intents = intents)


# Send error message if unknown command is received
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')
        await asyncio.sleep(int(2))
        await ctx.channel.purge(limit=1)
        await asyncio.sleep(int(0.25))
        await ctx.channel.purge(limit=1)

# chat filter
# The word "swear" is added as a swear word for showcasing purposes.
with open('badwords.txt', 'r') as f:
    words = f.read()
    badwords = words.split()

@client.event
async def on_message(message):
    msg = message.content
    for word in badwords:
        if word in msg:
            await message.delete()
            await message.channel.send("Dont use that word!")
            await asyncio.sleep(int(2))
            await message.channel.purge(limit=1)

    # await message.process_message(message)
    await client.process_commands(message)


# Load cogs (external code)
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

# Unload cogs (external code)
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run("OTczNjU4MjE3MjAyNzI0OTc0.GHqLzN.D6ZVEwlSDa3YJATO5RS3LkRQNeWQAHX_yc67zY")