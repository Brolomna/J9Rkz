import asyncio
import discord
from cog import Cog
from discord.utils import get

staff_room_id = 446525801920331776


class AntiRaidRobo(Cog):
    """
    A simple Cog to prevent automated raids.
    It works by saving new members in a list every 3 seconds and then banning them if the count is more than 5.

    TODO: Disable it when advertising or promoting the server anywhere(paid shoutouts,partnerships etc)
    """

    def __init__(self, bot):
        super().__init__(bot)
        self.bot = bot
        self.new_members = []
        self.join_wait_task = self.bot.loop.create_task(self.join_wait())

    def cog_unload(self):
        self.join_wait_task.cancel()

    @Cog.listener()
    async def on_member_join(self, member):
        self.new_members.append(member)

    async def join_wait(self):
        await self.bot.wait_until_ready()
        await asyncio.sleep(10)

        while not self.bot.is_closed():
            self.bot.loop.create_task(self.handle_joins())
            await asyncio.sleep(3)

    async def handle_joins(self):
        new_members_copy = self.new_members.copy()
        self.new_members.clear()

        if new_members_copy:
            if len(new_members_copy) >= 5:
                for member in new_members_copy:
                    try:
                        await member.ban(reason="Raid")
                    except (discord.NotFound, discord.Forbidden, discord.HTTPException) as e:
                        print(f"Error occurred in {__name__}:\n {e}")
                    except Exception as e:
                        print(
                            f"Unknown error occurred while banning members in {__name__}:", e)
                staff_room = get(
                    new_members_copy[0].guild.channels, id=staff_room_id)
                await staff_room.send(f"Hello lads! I banned **{len(new_members_copy)}** raiders 😎")


def setup(bot):
    bot.add_cog(AntiRaidRobo(bot))
