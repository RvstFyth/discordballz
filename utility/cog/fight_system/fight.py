"""
The :class:`Fight()` manages a fight, from the beginning to the end and returns the winner.

--

Author : DrLarck

Last update : 04/09/19 (DrLarck)
"""

# dependancies
import asyncio

# utility
from utility.cog.fight_system.phase_trigger import Trigger_phase
from utility.cog.fight_system.phase_selection import Selection_phase
from utility.cog.fight_system.phase_battle import Battle_phase

from utility.cog.displayer.team import Team_displayer

# translation
from utility.translation.translator import Translator

# fight manager
class Fight:
    """
    Manages a fight and returns the winner.

    - Parameter :

    `client` : Represents a `discord.Client`

    `ctx` : Represents the `commands.Context`

    `caller` : Represents the player that has called the class

    - Method :

    :coro:`get_average_hp(team)` : Returns the average hps of both teams

    :coro:`run_fight(team)` : Run a fight
    """

    # attribute
    def __init__(self, client, ctx, caller):
        self.client = client
        self.ctx = ctx
        self.player = caller

        # phase
        self.trigger_phase = None
        self.selection_phase = None
        self.battle_phae = None
    
    # method
    async def get_teams_hp(self, team):
        """
        `coroutine`

        Calculates then return the hp of each team.

        --

        Return : int, int (team_a then team_b)
        """

        # init
        team_a_average_hp = 0
        team_b_average_hp = 0

        # get the average team hps
            # for team_a
        for character_a in team[0]:
            await asyncio.sleep(0)

            team_a_average_hp += character_a.health.current

            # for team_b
        for character_b in team[1]:
            await asyncio.sleep(0)

            team_b_average_hp += character_b.health.current

        return(team_a_average_hp, team_b_average_hp)

    async def run_fight(self, team):
        """
        `coroutine`
        
        This method run the fight and manages the when the phases are called.

        - Parameter : 

        `team` : Represents a list of `team`s. The teams are `list` of :class:`Character()`.

        --

        Return : Winner index (0 or 1, 2 in case of a draw)

        0 : Caller
        1 : Enemy
        2 : Draw
        """

        # init
            # translation
        translation = Translator(self.client.db, self.player)
        #_ = await translation.translate()

            # turn displaying
        turn = 1  # begins at 1

            # init at 1 to loop at least one time
        team_a_average_hp = 1  
        team_b_average_hp = 1

            # determines the number of characters in each team
        team_a_length = len(team[0])
        team_b_length = len(team[1])

        # init
        # team a
        for character in team[0]:
            await asyncio.sleep(0)

            if(character != None):
                await character.init()
            
            else:
                team[0].remove(character)
        
        # team_b
        for _character in team[1]:
            await asyncio.sleep(0)
            
            if(_character != None):
                await _character.init()
            
            else:
                team[1].remove(_character)

        #########################################################################
        # main loop
        while(team_a_average_hp > 0 and team_b_average_hp > 0):  # if one of the teams is defeated, stops the loop
            await asyncio.sleep(0)

            # display
            displayer = Team_displayer(
                self.client,
                self.ctx,
                self.player,
                team[0],
                team[1]
            )
            
            # subclasses
            self.selection_phase = Selection_phase(self.client, self.ctx, self.player, turn)
            self.battle_phae = Battle_phase(self.client, self.ctx, self.player, None)

            # new turn
            await self.ctx.send(f"```########## 📣 Round {turn} ! ##########```")
            await asyncio.sleep(2)
            # team displaying
            await self.ctx.send("```👥 Teams```")
            await asyncio.sleep(1)
            await displayer.display_teams()

                # phases
            await self.ctx.send(f"```💠 - Selection phase```")
            await asyncio.sleep(1)

            # get move
                # team a
            team_a_move = await self.selection_phase.start_selection(team[0], team)
                # check if the player want to flee
            if(type(team_a_move) == str):
                if(team_a_move.lower() == "flee"):
                    await self.ctx.send(f"<@{self.player.id}> You flee the fight ...")
                    break

                # team b
            team_b_move = await self.selection_phase.start_selection(team[1], team)

            # battle phase
            await self.ctx.send(f"```⚔ - Battle phase```")
            await asyncio.sleep(2)

            print(f"Team_a_move : {team_a_move}\nTeam_b_move : {team_b_move}")
            await self.battle_phae.start_battle(team, team_a_move, team_b_move, turn)

            # trigger phase
            await self.ctx.send("```🌀 - Trigger phase```")
            await asyncio.sleep(1)

            character_index = 1

                # team_a
            await self.ctx.send(f"```🔵 - {self.player.name}'s team```")
            await asyncio.sleep(1)
            self.trigger_phase = Trigger_phase(team[0], team[1])

            for character_a in team[0]:
                await asyncio.sleep(0)

                await self.trigger_phase.trigger_effect(self.ctx, character_index, character_a)

                character_index += 1

                # team_b
            await self.ctx.send(f"```🔴 - Enemy team```")
            await asyncio.sleep(1)
            self.trigger_phase = Trigger_phase(team[1], team[0])

            for character_b in team[1]:
                await asyncio.sleep(0)

                await self.trigger_phase.trigger_effect(self.ctx, character_index, character_b)

                character_index += 1

            # end of turn
                # calculate average hps
            team_a_average_hp, team_b_average_hp = await self.get_teams_hp(team)

                # increase the turn value
            turn += 1
            print(f"team hps, a : {team_a_average_hp}, b : {team_b_average_hp}")
            await asyncio.sleep(5)
        
        # check the winner
        # player : 
        if(team_a_average_hp > 0 and team_b_average_hp <= 0):
            await self.ctx.send(f"<@{self.player.id}> The player 🔵**{self.player.name}** has won the fight !")
            return(0)
        
        # enemy :
        if(team_b_average_hp > 0 and team_a_average_hp <= 0):
            await self.ctx.send(f"<@{self.player.id}> The 🔴**Enemy team** has won the fight ! ")
            return(1)
        
        # draw
        if(team_a_average_hp <= 0 and team_b_average_hp <= 0):
            await self.ctx.send(f"<@{self.player.id}> Draw !")
            return(2)

        return