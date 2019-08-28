"""
This command allows the player to level up his characters.

--

Author : DrLarck

Last update : 16/08/19 (DrLarck)
"""

# dependancies
import asyncio

from discord.ext import commands

# utils
from utility.cog.fight_system.fight import Fight
    #checker
from utility.command.checker.basic import Basic_checker
    # translation
from utility.translation.translator import Translator

# test
from utility.cog.character.list.c1 import Character_1

# command
class Cmd_train(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @commands.command()
    async def train(self, ctx):
        """
        `coroutine`

        Start a fight against an adaptative team.

        The opponent team level is scaled on the player team level, same for the rarity.

        If the player wins the fight, his character gain some xp.
        """

        caller = ctx.message.author 

        # test shit
        chara = Character_1()
        charb = Character_1()
        charc = Character_1()

        ea = Character_1()
        ea.is_npc = True
        eb = Character_1()
        eb.is_npc = True
        ec = Character_1()
        ec.is_npc = True

        caller_team = [chara, charb, charc]
        enemy_team = [ea, eb, ec]

        for char in caller_team:
            await char.init()
        
        for char_b in enemy_team:
            await char_b.init()

        team = [caller_team, enemy_team]

        fight = Fight(self.client, ctx, caller)
        await fight.run_fight(team)
        
        return

def setup(client):
    client.add_cog(Cmd_train(client))