import discord
from discord.ext import commands
from discord import Member

class Cog6(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Duplicate Messages Command
    @commands.command(aliases=['scs', 'send', 'scm'])
    @commands.has_permissions(manage_messages=True)
    async def shortcut_send(self, ctx, amount, anonymous='n', *, content):
        await ctx.channel.purge(limit=1)
        amount = int(amount)
        if amount > 200:
            await ctx.send('200 is the MAX amount of messages you can send at a time!')
        else:
            if anonymous.lower() == 'a' or anonymous.lower() == 'y' or anonymous.lower() == 'yes':
                await ctx.send('Someone anonymously sent:')
                for i in range(0, amount):
                    await ctx.send(content)
            else:
                author = ctx.author
                author = str(author)
                await ctx.send(author[:-5] + ' sent:')
                for i in range(0, amount):
                    await ctx.send(content)


def setup(client):
    client.add_cog(Cog6(client))