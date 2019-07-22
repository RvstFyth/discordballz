"""
Manages the battle phase.

-- 

Author : DrLarck

Last update : 21/07/19
"""

# dependancies
import asyncio
from random import randint

# utils
from utility.cog.fight_system.calculator.damage import Damage_calculator
from utility.cog.displayer.move import Move_displayer

# embed
from utility.graphic.embed import Custom_embed

# battle phase manager
class Battle_phase:
    """
    Manages the battle phase.

    - Parameter : 

    - Attribute : 

    - Method :
    """

    # attribute
    def __init__(self, client, ctx, player_a, player_b):
        self.client = client
        self.ctx = ctx
        self.player_a = player_a
        self.player_b = player_b
    
    # method
    async def start_battle(self, team, team_a_move, team_b_move, turn):
        """
        `coroutine`

        Runs the battle phase.

        - Parameter :

        `team` : Represents a list of unit.

        `team_a_move` | `team_b_move` : Represents a dict of move.
        --

        Return : None
        """

        # init
        _move_display = Move_displayer()
        team_a = {
            "index" : 0,
            "display" : ""
        }

        team_b= {
            "index" : 0,
            "display" : ""
        }

        unit_index = 1

        # battle
        # team a
        await self.ctx.send(f"```🔵 - {self.player_a.name}\'s team```")
        
        for character in team[0]:
            await asyncio.sleep(0)

            # check if the character is able to fight
            if(character.health.current > 0 and character.posture.stunned == False):
                character_move = team_a_move[team_a["index"]]

                # set the target display
                if(character_move["target"] == None):  # if there is no target
                    team_a["display"] += f"\n{unit_index}. {character.image.icon}**{character.info.name}**{character.type.icon} to **Himself** :\n"
                
                else:
                    team_a["display"] += f"\n{unit_index}. {character.image.icon}**{character.info.name}**{character.type.icon} to {character_move['target'].image.icon}**{character_move['target'].info.name}**{character_move['target'].type.icon} :\n"
                
                # manage the move
                print(f"move : {character_move['move']} {type(character_move['move'])}")
                if(character_move["move"] == 1):  # sequence
                    await character.posture.change_posture("attacking")

                    # damage
                    damager = Damage_calculator(character, character_move["target"])

                    # generate a random number of damage
                    sequence_damage = randint(character.damage.physical_min, character.damage.physical_max)
                    damage_done = await damager.physical_damage(sequence_damage)

                    # inflict the damage
                    await character_move["target"].receive_damage(damage_done["calculated"])
                    
                    # prepare the move info
                    move_info = {
                        "name" : "Sequence",
                        "icon" : "👊",
                        "damage" : damage_done["calculated"],
                        "critical" : damage_done["critical"],
                        "dodge" : damage_done["dodge"],
                        "physical" : True,
                        "ki" : False
                    }

                    # displays the move
                    team_a["display"] += await _move_display.offensive_move(move_info)
                
                if(character_move["move"] == 2):  # charging ki
                    await character.posture.change_posture("charging")

                    # init 
                        # get the missing ki of the character
                    missing_ki = character.ki.maximum - character.ki.current
                        # take 10 % of the missing ki
                    missing_ki *= 0.1

                    # get the ki gain
                    # based on misisng ki and rarity of the character
                    ki_gain = int(randint(1, 5) + character.rarity.value + missing_ki)

                    # add the ki to the character
                    character.ki.current += ki_gain
                    await character.ki.ki_limit()

                    # prepare the move info
                    move_info = {
                        "name" : "Ki charge",
                        "icon" : "🔥",
                        "damage" : ki_gain,
                        "critical" : False,
                        "dodge" : False,
                        "physical" : False,
                        "ki" : False
                    }

                    team_a["display"] += await _move_display.ki_move(move_info)

            # update the index
            team_a["index"] += 1
            unit_index += 1
        
        # display the team_a move
        # test
        if(turn > 1):
            team_a_embed = Custom_embed(self.client)
            team_a_embed = await team_a_embed.setup_embed()

            print(f"Team_display : {team_a['display']}")
            team_a_embed.add_field(
                name = f"{self.player_a.name} team :",
                value = team_a["display"],
                inline = False
            )

            await self.ctx.send(embed = team_a_embed)
        
        return