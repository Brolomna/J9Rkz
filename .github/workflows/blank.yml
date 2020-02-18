import re
import discord
import random
import time
import asyncio
import aiohttp
import asyncpg
import datetime
from discord.ext import commands
from discord.utils import get
from cog import Cog

MENTION_RE = re.compile(r"<@(!?)([0-9]*)>")


def percentage(quota, messages):
    return int((messages / quota) * 100)


class Gangs(Cog):
    def __init__(self, bot):
        super().__init__(bot)
        self.bot = bot

    @commands.command(name="20+", aliases=['20'])
    async def twenty_plus(self, ctx, leave: str = None):
        """Join the 20+ gang"""
        if leave == "leave":
            return await ctx.author.edit(nick=None)
        nick = ctx.author.display_name

        if "20+" in nick:
            return await ctx.send(f"You are already in 😎 {ctx.author.mention}")

        else:
            if len(ctx.author.display_name) > 21:
                nick = ctx.author.display_name[:21]

        try:
            count = [m for m in ctx.guild.members if "20+" in m.display_name]
            await ctx.author.edit(nick=f"{nick} (20+ gang)")
            await ctx.channel.send(
                f"You have joined the **20+ gang** gang. ({len(count)} members) {ctx.author.mention}")
        except Exception as e:
            print(e)

    @commands.command(name="thigh")
    async def thigh(self, ctx, leave: str = None):
        """Join the thigh gang"""
        if leave == "leave":
            return await ctx.author.edit(nick=None)
        nick = ctx.author.display_name

        if "thigh" in nick:
            return await ctx.send(f"You are already in 😎 {ctx.author.mention}")

        else:
            if len(ctx.author.display_name) > 19:
                nick = ctx.author.display_name[:19]

        try:
            count = [m for m in ctx.guild.members if "thigh" in m.display_name]
            await ctx.author.edit(nick=f"{nick} (thigh gang)")
            await ctx.channel.send(
                f"You have joined the **thigh gang** gang. ({len(count)} members) {ctx.author.mention}")
        except Exception as e:
            print(e)

    @commands.command(name="bruh")
    async def bruh(self, ctx, leave: str = None):
        """Join the bruh gang"""
        if leave == "leave":
            return await ctx.author.edit(nick=None)
        nick = ctx.author.display_name

        if "bruh" in nick:
            return await ctx.send(f"You are already in 😎 {ctx.author.mention}")

        else:
            if len(ctx.author.display_name) > 20:
                nick = ctx.author.display_name[:20]

        try:
            count = [m for m in ctx.guild.members if "bruh" in m.display_name]
            await ctx.author.edit(nick=f"{nick} (bruh gang)")
            await ctx.channel.send(
                f"You have joined the **bruh gang** gang. ({len(count)} members) {ctx.author.mention}")
        except Exception as e:
            print(e)


    @commands.command(name="sip")
    async def sip(self, ctx, leave: str = None):
        """Join the SIP gang"""
        if leave == "leave":
            return await ctx.author.edit(nick=None)
        nick = ctx.author.display_name

        if "SIP" in nick:
            return await ctx.send(f"You are already in 😎 {ctx.author.mention}")

        else:
            if len(ctx.author.display_name) > 26:
                nick = ctx.author.display_name[:26]

        try:
            count = [m for m in ctx.guild.members if "SIP" in m.display_name]
            await ctx.author.edit(nick=f"{nick} (SIP)")
            await ctx.channel.send(
                f"You have joined the **SIP gang** gang. ({len(count)} members) {ctx.author.mention}")
        except Exception as e:
            print(e)

    @commands.command(name="potato", aliases=['🥔'])
    # @commands.cooldown(1, 5000, commands.BucketType.user)
    async def potato(self, ctx, leave: str = None):
        """Join the potato gang"""
        if leave == "leave":
            return await ctx.author.edit(nick=None)
        nick = ctx.author.display_name

        if "gang" in ctx.author.display_name:
            if "(" in ctx.author.display_name:
                nick = ctx.author.display_name.split('(')[0].strip()

        elif len(ctx.author.display_name) > 18:
            nick = ctx.author.display_name[:18]

        try:
            await ctx.author.edit(nick=f"{nick} (Potato Gang)")
            await ctx.channel.send(f"You have successfully joined the **Potato Gang** {ctx.author.mention}")
        except Exception as e:
            print(e)

    @commands.command(name="tbc", aliases=['thotboiclique'])
    # @commands.cooldown(1, 5000, commands.BucketType.user)
    async def tbc(self, ctx, leave: str = None):
        """Join the thotboiclique gang"""
        if leave == "leave":
            return await ctx.author.edit(nick=None)
        nick = ctx.author.display_name

        if "thotboiclique" in nick.lower():
            return await ctx.send(f"You are already in 😎 {ctx.author.mention}")

        else:
            if len(ctx.author.display_name) > 16:
                nick = ctx.author.display_name[:16]

        try:
            count = [m for m in ctx.guild.members if "thotboiclique" in m.display_name.lower()]
            await ctx.author.edit(nick=f"{nick} (thotboiclique)")
            await ctx.channel.send(f"You have joined the **thotboiclique** gang. ({len(count)} members) {ctx.author.mention}")
        except Exception as e:
            print(e)

    @commands.command(name="emg", aliases=['emagine'])
   #  @commands.cooldown(1, 5000, commands.BucketType.user)
    async def emg(self, ctx, leave: str = None):
        """Join the e-magine gang"""
        if leave == "leave":
            return await ctx.author.edit(nick=None)
        nick = ctx.author.display_name

        if "e-magine" in nick.lower():
            return await ctx.send(f"You are already in 😎 {ctx.author.mention}")

        else:
            if len(ctx.author.display_name) > 16:
                nick = ctx.author.display_name[:16]

        try:
            count = [m for m in ctx.guild.members if "e-magine" in m.display_name.lower()]
            await ctx.author.edit(nick=f"{nick} (e-magine gang)")
            await ctx.channel.send(
                f"You have joined the **e-magine** gang. ({len(count)} members) {ctx.author.mention}")
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(Gangs(bot))
