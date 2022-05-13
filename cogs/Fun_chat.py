import discord
from discord.ext import commands
import random
class Cog4(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Magic 8ball Command
    # Usage:
    # >8ball <question>
    @commands.command(aliases=['8ball', '?'])
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes - definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     "Don't count on it.",
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']
        await ctx.channel.purge(limit=1)
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    
    
    # Gif Commands
    @commands.command(aliases=['okay', 'OK'])
    @commands.has_permissions(change_nickname=True)
    async def ok(self, ctx):
        await ctx.channel.purge(limit=1)
        author = ctx.author
        author = str(author)
        await ctx.send(author[:-5] + ' says: OK!')
        await ctx.send('https://tenor.com/view/ok-okay-gif-5307535')
        await ctx.send('‎')

    @commands.command(aliases=['YES', 'y', 'ye'])
    @commands.has_permissions(change_nickname=True)
    async def yes(self, ctx):
        await ctx.channel.purge(limit=1)
        author = ctx.author
        author = str(author)
        await ctx.send(author[:-5] + ' says: Yes!')
        await ctx.send('https://tenor.com/view/yes-baby-goal-funny-face-gif-13347383')
        await ctx.send('‎')

    @commands.command(aliases=['NO', 'n'])
    @commands.has_permissions(change_nickname=True)
    async def no(self, ctx):
        await ctx.channel.purge(limit=1)
        author = ctx.author
        author = str(author)
        await ctx.send(author[:-5] + ' says: No!')
        await ctx.send('https://tenor.com/view/no-nooo-nope-eat-fingerwag-gif-4880183')
        await ctx.send('‎')

    @commands.command(aliases=['hello', 'hey'])
    @commands.has_permissions(change_nickname=True)
    async def hi(self, ctx):
        await ctx.channel.purge(limit=1)
        author = ctx.author
        author = str(author)
        await ctx.send(author[:-5] + ' says: Hi!')
        await ctx.send('https://tenor.com/view/guys-gif-4440552')
        await ctx.send('‎')

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def oops(self, ctx):
        await ctx.channel.purge(limit=1)
        author = ctx.author
        author = str(author)
        await ctx.send(author[:-5] + ' says: Oops!')
        await ctx.send('https://tenor.com/view/kid-run-hallway-oops-walking-back-gif-12263463')
        await ctx.send('‎')


def setup(client):
    client.add_cog(Cog4(client))