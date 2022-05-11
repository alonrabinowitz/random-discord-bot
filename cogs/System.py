import discord
from discord.ext import commands


class Cog1(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('RDB is ready.')

    # Member Join and Leave
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')

    @commands.command()
    async def ping(self, ctx):
        # await ctx.send('pong')
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(Cog1(client))