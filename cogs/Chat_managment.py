import discord
from discord.ext import commands
import asyncio

class Cog2(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['c'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount + 1)
        if amount == 1:
            await ctx.send('A message was deleted.')
        elif amount > 1:
            await ctx.send(f'{amount} messages were deleted.')
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=1)


    @commands.command(aliases=['ca', 'clear all', 'clearall'])
    @commands.has_permissions(manage_messages=True)
    async def clear_all(self, ctx):
        await ctx.channel.purge(limit=10000000001)
        await ctx.send('Chat has been cleared.')
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=1)

def setup(client):
    client.add_cog(Cog2(client))