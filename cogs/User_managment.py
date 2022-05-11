import discord
from discord.ext import commands
import asyncio
from discord import Member, Role

class Cog3(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Kick Command
    @commands.command(aliases=['k'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason='Oops someone forgot to put one in!'):
        await member.kick(reason=reason)
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{member} has been kicked for the reason: ' + reason)

    # Add and Remove Roles
    @commands.command(aliases=['add_role', 'AddRole', 'ar'])
    @commands.has_permissions(manage_roles=True)
    async def add_role_command(self, ctx, member: Member, *, role: Role):
        await member.add_roles(role)

    @commands.command(aliases=['remove_role', 'RemoveRole', 'rr'])
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member: Member, *, role: Role):
        await member.remove_roles(role)

    @commands.command(aliases=['remove_all_roles', 'rar'])
    @commands.has_permissions(administrator=True)
    async def removeallroles(self, ctx, member: Member):
        member_role_list = member.roles
        member_amount_of_roles = len(member_role_list)
        for r in range(1, member_amount_of_roles):
            await member.remove_roles(member_role_list[r])

    # Mute and Unmute Commands
    @commands.command(aliases=['amr', 'am'])
    @commands.has_permissions(administrator=True)
    async def addmuterole(self, ctx, member: Member):
        print(member)
        role = 'MUTED'
        await member.add_roles(role)
        # await member.add_roles(role)
        print('sdg')

    @commands.command(aliases=['m'])
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: Member, *, reason='Oops! Seems like someone forgot to put one in!'):
        await self.removeallroles(ctx, member)
        muted_role = discord.utils.get(member.guild.roles, name='MUTED')
        await member.add_roles(muted_role)
        await ctx.send(f'{member} has been muted. Reason: {reason}')
        print(f'{member} has been muted.')

    @commands.command(aliases=['um', 'unm'])
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: Member):
        await self.removeallroles(ctx, member)
        member_role = discord.utils.get(member.guild.roles, name='MEMBER')
        print(f'{member} has been unmuted!')
        await member.add_roles(member_role)

    @commands.command(aliases=['mt'])
    @commands.has_permissions(administrator=True)
    async def mutetimer(self, ctx, member: Member, timeperiod, timeunit,
                        *, reason='Oops! Seems like someone forgot to put one in!'):
        memberroles = member.roles
        memberamountofroles = len(memberroles)
        print(memberroles)
        await self.removeallroles(ctx, member)
        muted_role = discord.utils.get(member.guild.roles, name='MUTED')
        await member.add_roles(muted_role)
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{member} has been muted for {timeperiod}{timeunit}. Reason: {reason}')
        if timeunit.lower() == 's' or timeunit.lower() == 'second' or timeunit.lower() == 'seconds':
            # time.sleep(int(timeperiod))
            await asyncio.sleep(int(timeperiod))
            # t = Timer(int(timeperiod), party_time, args=None, kwargs=None)
            # t.start()
            await self.removeallroles(ctx, member)
            # member_role = discord.utils.get(member.guild.roles, name='MEMBER')
            # await member.add_roles(member_role)
            print(f'{member} has been unmuted.')
            for r in range(1, memberamountofroles):
                await member.add_roles(memberroles[r])
            await ctx.send(f"{member}'s {timeperiod}{timeunit} mute timer has run out. {member} is now unmuted!")
        elif timeunit.lower() == 'm' or timeunit.lower() == 'minute' or timeunit.lower() == 'minutes':
            await asyncio.sleep(int(timeperiod) * 60)
            await self.removeallroles(ctx, member)
            # member_role = discord.utils.get(member.guild.roles, name='MEMBER')
            # await member.add_roles(member_role)
            # await member.add_roles(memberroles)
            print(f'{member} has been unmuted.')
            for r in range(1, memberamountofroles):
                await member.add_roles(memberroles[r])
            await ctx.send(f"{member}'s {timeperiod}{timeunit} mute timer has run out. {member} is now unmuted!")
        elif timeunit.lower() == 'h' or timeunit.lower() == 'hour' or timeunit.lower() == 'hours':
            await asyncio.sleep(int(timeperiod) * 3600)
            await self.removeallroles(ctx, member)
            # member_role = discord.utils.get(member.guild.roles, name='MEMBER')
            # await member.add_roles(member_role)
            # await member.add_roles(memberroles)
            print(f'{member} has been unmuted.')
            for r in range(1, memberamountofroles):
                await member.add_roles(memberroles[r])
            await ctx.send(f"{member}'s {timeperiod}{timeunit} mute timer has run out. {member} is now unmuted!")
        elif timeunit.lower() == 'd' or timeunit.lower() == 'day' or timeunit.lower() == 'days':
            await asyncio.sleep(int(timeperiod) * 86400)
            await self.removeallroles(ctx, member)
            # member_role = discord.utils.get(member.guild.roles, name='MEMBER')
            # await member.add_roles(member_role)
            # await member.add_roles(memberroles)
            print(f'{member} has been unmuted.')
            for r in range(1, memberamountofroles):
                await member.add_roles(memberroles[r])
            await ctx.send(f"{member}'s {timeperiod}{timeunit} mute timer has run out. {member} is now unmuted!")
        else:
            await asyncio.sleep(int(timeperiod))
            await self.removeallroles(ctx, member)
            # member_role = discord.utils.get(member.guild.roles, name='MEMBER')
            # await member.add_roles(member_role)
            # await member.add_roles(memberroles)
            print(f'{member} has been unmuted.')
            for r in range(1, memberamountofroles):
                await member.add_roles(memberroles[r])
            await ctx.send(f"{member}'s {timeperiod}{timeunit} mute timer has run out. {member} is now unmuted!")

    # Ban and Unban Commands
    @commands.command(aliases=['b'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason='Oops someone forgot to input a reason!'):
        await member.ban(reason=reason)
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{member} has been banned for the reason: ' + reason)

    @commands.command(aliases=['ub'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        print('t')
        member_name, member_discriminator = member.split('#')
        print('h')
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Yay! {user.name}#{user.discriminator} has been unbanned. He can rejoin now!')
                return

def setup(client):
    client.add_cog(Cog3(client))