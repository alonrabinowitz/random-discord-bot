import asyncio
import os
import discord
from discord.ext import commands

#Alon R and Alon F

intents = discord.Intents.all()

client = commands.Bot(command_prefix = '>', intents = intents)


# @client.event
# async def on_ready():
#     print('RDB is ready.')

# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined a server.')
#
# @client.event
# async def on_member_remove(member):
#     print(f'{member} has left a server.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')
        await asyncio.sleep(int(2))
        await ctx.channel.purge(limit=1)
        await asyncio.sleep(int(0.25))
        await ctx.channel.purge(limit=1)


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run("OTczNjU4MjE3MjAyNzI0OTc0.GHqLzN.D6ZVEwlSDa3YJATO5RS3LkRQNeWQAHX_yc67zY")