"""
This command allows the player to level up his characters.

--

Author : DrLarck

Last update : 14/07/19
"""

# dependancies
import asyncio

from discord.ext import commands

# translation
from utility.translation.translator import Translator

# command
class Cmd_train(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def train(self, ctx):
        """
        `coroutine`

        Start a fight against an adaptative team.

        The opponent team level is scaled on the player team level, same for the rarity.

        If the player wins the fight, his character gain some xp.
        """

        translator = Translator(self.client.db, ctx.message.author)
        _ = await translator.translate()

        await ctx.send(_(f"<@{ctx.message.author.id}> Hello"))
        
        return

def setup(client):
    client.add_cog(Cmd_train(client))