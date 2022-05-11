import discord
from discord.ext import commands
import random

class Cog5(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Rock Paper Scissors Game Command
    @commands.command(aliases=['rps', 'rpsgame', 'rps_game'])
    async def rockpaperscissors_game(self, ctx, choice):
        rockpaperscissors_random = random.randint(1, 3)
        # 1 = rock, 2= paper, 3 = scissors
        if rockpaperscissors_random == 1:
            if choice.lower() == "rock" or choice.lower() == "r":
                await ctx.send('My choice is Rock.')
                await ctx.send("You chose Rock too?!? we got a tie!")
            elif choice.lower() == "paper" or choice.lower() == "p":
                await ctx.send('My choice is Rock.')
                await ctx.send("You chose Paper?!? Nice! You WON!")
            elif choice.lower() == "scissors" or choice.lower() == "s":
                await ctx.send('My choice is Rock.')
                await ctx.send("You chose Scissors?!? OMG! I WON!")
            else:
                await ctx.send(
                    f"ehhh, seems like you didn't pick a supported choice. The supported choices are: 'rock'('r'), 'paper'('p'), and 'scissors'('s'). What the flip is '{choice}'")
        elif rockpaperscissors_random == 2:
            if choice.lower() == "paper" or choice.lower() == "p":
                await ctx.send('My choice is Paper.')
                await ctx.send("You chose Paper too?!? we got a tie!")
            elif choice.lower() == "scissors" or choice.lower() == "s":
                await ctx.send('My choice is Paper.')
                await ctx.send("You chose Scissors?!? Nice! You WON!")
            elif choice.lower() == "rock" or choice.lower() == "r":
                await ctx.send('My choice is Paper.')
                await ctx.send("You chose Rock?!? OMG! I WON!")
            else:
                await ctx.send(
                    f"ehhh, seems like you didn't pick a supported choice. The supported choices are: 'rock'('r'), 'paper'('p'), and 'scissors'('s'). What the flip is '{choice}'")
        elif rockpaperscissors_random == 3:
            if choice.lower() == "scissors" or choice.lower() == "s":
                await ctx.send('My choice is Scissors.')
                await ctx.send("You chose Scissors too?!? we got a tie!")
            elif choice.lower() == "rock" or choice.lower() == "r":
                await ctx.send('My choice is Scissors.')
                await ctx.send("You chose Rock?!? Nice! You WON!")
            elif choice.lower() == "paper" or choice.lower() == "p":
                await ctx.send('My choice is Scissors.')
                await ctx.send("You chose Paper?!? OMG! I WON!")
            else:
                await ctx.send(
                    f"ehhh, seems like you didn't pick a supported choice. The supported choices are: 'rock'('r'), 'paper'('p'), and 'scissors'('s'). What the flip is '{choice}'")

    # Get On Top Game Command
    @commands.command(aliases=['got'])
    async def get_on_top_gamecommand(self, ctx, which):
        if which == '1':
            await ctx.send(f'{ctx.author} wanted to play Get On Top 1, so here you go:')
            await ctx.send('https://www.twoplayergames.org/Get-on-Top/904.html')
        elif which == '2':
            await ctx.send(f'{ctx.author} wanted to play Get On Top 2, so here you go: ')
            await ctx.send('https://getontop2.com/')
        elif which == '3':
            await ctx.send(f'{ctx.author} wanted to play Get On Top 3, so here you go: ')
            await ctx.send('https://www.crazygames.com/game/get-on-top')
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("This does not exist. Why make up random stuff?")

def setup(client):
    client.add_cog(Cog5(client))