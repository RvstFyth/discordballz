"""
This command allows the player to level up his characters.

--

Author : DrLarck

Last update : 01/09/19 (DrLarck)
"""

# dependancies
import asyncio

from discord.ext import commands

# utils
from utility.cog.fight_system.fight import Fight
from utility.cog.player.player import Player
from utility.cog.character.getter import Character_getter
from utility.command._train import Train
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
        tool = Train(self.client)

        # get caller team
        caller_team = await player.team.get_team()
        caller_team = [
            await getter.get_from_unique(self.client, caller_team["a"]),
            await getter.get_from_unique(self.client, caller_team["b"]),
            await getter.get_from_unique(self.client, caller_team["c"])
        ]

        # get opponent team
        opponent_team = await tool.generate_opponent_team(player)

        team = [caller_team, opponent_team]

        fight = Fight(self.client, ctx, player)
        await fight.run_fight(team)
        
        return

def setup(client):
    client.add_cog(Cmd_train(client))