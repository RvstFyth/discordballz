"""
The :class:`Fight()` manages a fight, from the beginning to the end and returns the winner.

--

Author : DrLarck

Last update : 16/08/19 (DrLarck)
"""

# dependancies
import asyncio

# utility
from utility.cog.fight_system.phase_trigger import Trigger_phase
from utility.cog.fight_system.phase_selection import Selection_phase
from utility.cog.fight_system.phase_battle import Battle_phase

# translation
from utility.translation.translator import Translator

# fight manager
class Fight:
    """
    Manages a fight and returns the winner.

    - Parameter :

    - Attribute : 

    - Method :
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
    async def get_average_hp(self, team):
        """
        `coroutine`

        Calculates then return the average hp of each team.

        --

        Return : int, int (team_a then team_b)
        """

        # init
        team_a_average_hp = 1
        team_b_average_hp = 1

        # determines the number of characters in each team
        team_a_length = len(team[0])
        team_b_length = len(team[1])

        # get the average team hps
            # for team_a
        for character_a in team[0]:
            await asyncio.sleep(0)

            team_a_average_hp += character_a.health.current

            # for team_b
        for character_b in team[1]:
            await asyncio.sleep(0)

            team_b_average_hp += character_b.health.current
        
        # get the average amount of hps
        team_a_average_hp = int(team_a_average_hp / team_a_length)
        team_b_average_hp = int(team_b_average_hp / team_b_length)

        return(team_a_average_hp, team_b_average_hp)

    async def run_fight(self, team):
        """
        `coroutine`
        
        This method run the fight and manages the when the phases are called.

        - Parameter : 

        `team` : Represents a list of `team`s. The teams are `list` of :class:`Character()`.

        --

        Return : Winner index (0 or 1, 2 in case of a draw)
        """

        # init
            # translation
        translation = Translator(self.client.db, self.player)
        #_ = await translation.translate()

            # turn displaying
        turn = 2  # begins at 1

            # init at 1 to loop at least one time
        team_a_average_hp = 1  
        team_b_average_hp = 1

            # determines the number of characters in each team
        team_a_length = len(team[0])
        team_b_length = len(team[1])

        # main loop
        while(team_a_average_hp > 0 and team_b_average_hp > 0):  # if one of the teams is defeated, stops the loop
            await asyncio.sleep(0)

            # subclasses
            self.selection_phase = Selection_phase(self.client, self.ctx, self.player, turn)
            self.battle_phae = Battle_phase(self.client, self.ctx, self.player, None)

            # new turn
            await self.ctx.send(f"########## 📣 Round {turn} ! ##########")
            await asyncio.sleep(2)

                # phases
            await self.ctx.send(f"💠 - Selection phase")
            await asyncio.sleep(1)

            # get move
            team_a_move = await self.selection_phase.start_selection(team[0], team)
                # check if the player want to flee
            if(type(team_a_move) == str):
                if(team_a_move.lower() == "flee"):
                    await self.ctx.send(f"<@{self.player.id}> You flee the fight ...")
                    break
            
            # battle phase
            await self.ctx.send(f"⚔ - Battle phase")
            await asyncio.sleep(2)

            await self.battle_phae.start_battle(team, team_a_move, None, turn)

            # trigger phase
            await self.ctx.send("🌀 - Trigger phase")
            await asyncio.sleep(1)

                # team_a
            await self.ctx.send(f"```🔵 - {self.player.name}'s team```")
            await asyncio.sleep(1)
            self.trigger_phase = Trigger_phase(team[0], team[1])

            for character_a in team[0]:
                await asyncio.sleep(0)

                await self.trigger_phase.trigger_effect(self.ctx, character_a)

                # team_b
            await self.ctx.send(f"```🔴 - Enemy team```")
            await asyncio.sleep(1)
            self.trigger_phase = Trigger_phase(team[1], team[0])

            for character_b in team[1]:
                await asyncio.sleep(0)

                await self.trigger_phase.trigger_effect(self.ctx, character_b)

            # end of turn
                # calculate average hps
            team_a_average_hp, team_b_average_hp = await self.get_average_hp(team)

                # increase the turn value
            turn += 1
            await asyncio.sleep(5)

        return