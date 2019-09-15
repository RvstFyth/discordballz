"""
The :class:`Fight()` manages a fight, from the beginning to the end and returns the winner.

--

Author : DrLarck

Last update : 15/09/19 (DrLarck)
"""

# dependancies
import asyncio

# utility
from utility.cog.fight_system.phase_trigger import Trigger_phase
from utility.cog.fight_system.phase_selection import Selection_phase
from utility.cog.fight_system.phase_battle import Battle_phase

from utility.cog.displayer.team import Team_displayer

from utility.cog.character.getter import Character_getter

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
    async def reset_stat(self, team):
        """
        `coroutine` 

        Reset the stats of the characters, except the current health.

        - Parameter :

        `team` : Represents the team to reset.

        --

        Return : None
        """

        # init
        character_getter = Character_getter()
        character_index = 0

        print("#################################################")

        # team a
        for char_a in team:
            await asyncio.sleep(0)

            # get the reference
            char_a_ref = await character_getter.get_character(char_a.info.id)

            # set the same stat as the char_a
            char_a_ref.level = char_a.level
            char_a_ref.rarity.value = char_a.rarity.value
            char_a_ref.enhancement = char_a.enhancement
            await char_a_ref.init()

            print(f"Reset :\nchar a : {char_a.info.id} | ref : {char_a_ref.info.id}\nA spirit : {char_a.defense.spirit} | B : {char_a_ref.defense.spirit}")

                # health
            char_a.health.maximum = char_a_ref.health.maximum

                # damage
            char_a.damage.physical_max = char_a_ref.damage.physical_max
            char_a.damage.physical_min = char_a_ref.damage.physical_min

            char_a.damage.ki_max = char_a_ref.damage.ki_max
            char_a.damage.ki_min = char_a_ref.damage.ki_min

                # defense
            char_a.defense.armor = char_a_ref.defense.armor
            char_a.defense.spirit = char_a_ref.defense.spirit
            char_a.defense.dodge = char_a_ref.defense.dodge

                # bonus
            char_a.critical_chance = char_a_ref.critical_chance
            char_a.critical_bonus = char_a_ref.critical_bonus
            char_a.regeneration.health = char_a_ref.regeneration.health
            char_a.regeneration.ki = char_a_ref.regeneration.ki

            character_index += 1

        return

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
        turn = 2  # begins at 1

            # init at 1 to loop at least one time
        team_a_average_hp = 1  
        team_b_average_hp = 1

        # init
        # team a
        team_a_ref = []
        for character in team[0]:
            await asyncio.sleep(0)

            if(character != None):
                await character.init()
                team_a_ref.append(character)
        
        team[0] = team_a_ref
        
        # team_b
        team_b_ref = []
        for _character in team[1]:
            await asyncio.sleep(0)
            
            if(_character != None):
                await _character.init()
                team_b_ref.append(_character)
        
        team[1] = team_b_ref

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
            if(turn == 1):
                await self.ctx.send("```👥 Teams```")
                await asyncio.sleep(1)
                await displayer.display_teams()

                # phases
            await self.ctx.send(f"```💠 - Selection phase```")
            await asyncio.sleep(1)

            # get move
                # team a
            team_a_move = await self.selection_phase.start_selection(0, team)
                # check if the player want to flee
            if(type(team_a_move) == str):
                if(team_a_move.lower() == "flee"):
                    await self.ctx.send(f"<@{self.player.id}> You flee the fight ...")
                    break

                # team b
            team_b_move = await self.selection_phase.start_selection(1, team)

            # battle phase
            await self.ctx.send(f"```⚔ - Battle phase```")
            await asyncio.sleep(2)

            await self.battle_phae.start_battle(team, team_a_move, team_b_move, turn)

            # reset stat
                # team a
            await self.reset_stat(team_a_ref)

                # team b
            await self.reset_stat(team_b_ref)

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