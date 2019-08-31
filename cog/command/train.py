"""
This command allows the player to level up his characters.

--

Author : DrLarck

Last update : 31/08/19 (DrLarck)
"""

# dependancies
import asyncio

from discord.ext import commands

# utils
from utility.cog.fight_system.fight import Fight
from utility.cog.player.player import Player
from utility.cog.character.getter import Character_getter
    #checker
from utility.command.checker.basic import Basic_checker
from utility.command.checker.fight import Fight_checker
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
    @commands.check(Fight_checker().has_team)
    @commands.command()
    async def train(self, ctx):
        """
        `coroutine`

        Start a fight against an adaptative team.

        The opponent team level is scaled on the player team level, same for the rarity.

        If the player wins the fight, his character gain some xp.
        """

        # init
        caller = ctx.message.author 
        player = Player(ctx, self.client, caller)
        getter = Character_getter()

        # get caller team
        caller_team = await player.team.get_team()
        caller_team = [
            await getter.get_from_unique(self.client, caller_team["a"]),
            await getter.get_from_unique(self.client, caller_team["b"]),
            await getter.get_from_unique(self.client, caller_team["c"])
        ]

        ea = Character_1()
        ea.is_npc = True
        eb = Character_1()
        eb.is_npc = True
        ec = Character_1()
        ec.is_npc = True

        enemy_team = [ea, eb, ec]

        for char in caller_team:
            await asyncio.sleep(0)

            if(char != None):
                await char.init()
            
            else:  # remove the None type
                caller_team.remove(char)
        
        for char_b in enemy_team:
            await asyncio.sleep(0)

            if(char_b != None):
                await char_b.init()
            
            else:
                enemy_team.remove(char_b)

        team = [caller_team, enemy_team]

        fight = Fight(self.client, ctx, player)
        await fight.run_fight(team)
        
        return

def setup(client):
    client.add_cog(Cmd_train(client))