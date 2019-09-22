"""
This command allows the player to level up his characters.

--

Author : DrLarck

Last update : 22/09/19 (DrLarck)
"""

# dependancies
import asyncio

from discord.ext import commands

# utils
from utility.cog.fight_system.fight import Fight
from utility.cog.player.player import Player
from utility.cog.character.getter import Character_getter
from utility.command._train import Train
from utility.cog.level.level import Leveller
    #checker
from utility.command.checker.basic import Basic_checker
from utility.command.checker.fight import Fight_checker
    # translation
from utility.translation.translator import Translator

# command
class Cmd_train(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.check(Basic_checker().is_game_ready)
    @commands.check(Basic_checker().is_registered)
    @commands.check(Fight_checker().is_in_fight)
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
        leveller = Leveller(self.client, ctx)

        # get caller team
        caller_team = await player.team.get_team()
        player_team = [
            await getter.get_from_unique(self.client, caller_team["a"]),
            await getter.get_from_unique(self.client, caller_team["b"]),
            await getter.get_from_unique(self.client, caller_team["c"])
        ]

        # get opponent team
        opponent_team = await tool.generate_opponent_team(player)

        team = [player_team, opponent_team]

        fight = Fight(self.client, ctx, player)

        await ctx.send(f"<@{player.id}> You enter in combat.")

        winner = await fight.run_fight(team)
        
        # redefine team
        caller_team = await player.team.get_team()
        
        # check winning condition
        id_team = [
            caller_team["a"], caller_team["b"], caller_team["c"]
        ]

        # set the xp
        # init
        xp_won = 100
        player_info = await player.team.get_info()
        player_team_level, player_team_rarity = player_info["level"], player_info["rarity"]

        # set the xp gain
        xp_won += (((1.5 * 100) - 100) * player_team_level) + (100 * (player_team_rarity - 1))

        if(winner == 0):  # if the player wins it
            # add xp
            await leveller.team_add_xp(player, id_team, xp_won)
        
        elif(winner == 2):  # if draw
            # half xp gained
            await leveller.team_add_xp(player, team, xp_won/2)

def setup(client):
    client.add_cog(Cmd_train(client))