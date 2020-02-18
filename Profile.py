import random
import aiohttp
import discord
import asyncio

from discord.ext import commands
from cog import Cog


class Profile(Cog):
    def __init__(self, bot):
        super().__init__(bot)
        self.bot = bot
        self.status_task = self.bot.loop.create_task(self.change_status())
        self.avatar_task = self.bot.loop.create_task(self.change_avatar())

    def cog_unload(self):
        self.status_task.cancel()
        self.avatar_task.cancel()

    @Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user} | Serving {len(self.bot.guilds)} servers.")

    async def change_status(self):
        await self.bot.wait_until_ready()
        await asyncio.sleep(5)

        last_mod = None

        def get_member_by_role(role_name):
            online_members = [m for m in self.bot.get_guild(self.bot.cc).members
                              if role_name in [r.name for r in m.roles]
                              and m.status in [discord.Status.online, discord.Status.dnd, discord.Status.idle]]

            if online_members:
                return random.choice(online_members).display_name
            else:
                return "members"

        while not self.bot.is_closed():
            mod_name = get_member_by_role("Staff")
            if mod_name != last_mod:
                await self.bot.change_presence(activity=discord.Activity(
                    type=discord.ActivityType.listening,
                    name=mod_name)
                )

                last_mod = mod_name

            await asyncio.sleep(5)

    async def change_avatar(self):
        await self.bot.wait_until_ready()
        await asyncio.sleep(5)

        wait_time = 3600

        while not self.bot.is_closed():
            async with aiohttp.ClientSession() as session:
                url = f"https://robohash.org/{random.random()}"
                async with session.get(url) as resp:
                    if resp.status == 200:
                        try:
                            await self.bot.user.edit(avatar=await resp.read())
                        except discord.errors.HTTPException as e:
                            print("Avatar error:", e)
                            wait_time += 3600
                    else:
                        print("Avatar error:", resp.reason, resp.status)

            await asyncio.sleep(wait_time)
            wait_time = 3600


def setup(bot):
    bot.add_cog(Profile(bot))
