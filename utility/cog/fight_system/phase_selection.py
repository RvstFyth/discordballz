"""
Manages the selection phase.

--

Author : DrLarck

Last update : 21/07/19 (DrLarck)
"""

# dependancies
import asyncio

# utils
    # translation
from utility.translation.translator import Translator

    # displayer
from utility.cog.displayer.character import Character_displayer
from utility.cog.displayer.team import Team_displayer

    # wait for
from utility.cog.fight_system.wait_for.player_choice import Player_choice

# selection phase manager
class Selection_phase:
    """
    Manages the selection phase.

    - Parameter :

    - Attribute :

    - Method :
    """

    # attribute
    def __init__(self, client, ctx, player, turn):
        self.client = client
        self.player = player
        self.ctx = ctx
        self.turn = turn

    # method
    async def start_selection(self, player_team, team):
        """
        `coroutine`

        Start the selection phase.

        --

        Return : None
        """

        # init
        translation = Translator(self.client.db, self.player)
        #_ = await translation.translate()
        order = 1  # display the character's order number 
        possible_action = []  # list of possible actions (str)
        all_character = team[0]+team[1]
        target_display = ""
        unit_index = 1
        
        # stores the move in it.
        move_list = []  # stores the move_choice

        # choice
        choice = Player_choice(self.client, self.player)

        for character in player_team:
            await asyncio.sleep(0)

            # init
            move_choice = {
                "move" : None,
                "target" : None
            }  

            if(character.health.current > 0 and character.posture.stunned == False):
                # displying the character
                displayer = Character_displayer(self.client, self.ctx, self.player)
                displayer.character = character

                await displayer.display(combat_format = True)
                await asyncio.sleep(2)

                # displaying the kit
                if(self.turn == 1):  # first turn
                    kit = "`1. Skip the turn ⏩` | "
                    kit += "`3. Defend 🏰`\n"

                    # init the possible actions
                    possible_action = ["check", "flee", "1", "3"]
        
                else:
                    kit = "`1. Sequence 👊` | "
                    kit += "`2. Ki charge 🔥` | "
                    kit += "`3. Defend 🏰`"

                    # init the possible actions
                    possible_action = ["check", "flee", "1", "2", "3"]

                    kit += "\n\n__Abilities__ :\n\n"
                    
                    if(len(character.ability) > 0):  # if the character has an ability
                        # init
                        ability_index = 4

                        for ability in character.ability:
                            await asyncio.sleep(0)

                            # add a new possible action
                            possible_action.append(str(ability_index))

                            kit += f"`{ability_index}. {ability.name}`{ability.icon}\n"
                            ability_index += 1
                
                kit += f"\nTo **flee** the fight, type `flee`, to **take a look at** a specific unit, type `check [unit index]`."
                
                # ask for the player's action
                decision = False

                while(decision == False):
                    await asyncio.sleep(0)

                    # display the actions
                    actions = f"<@{self.player.id}> Please select an action amoung the following for #{order} {character.image.icon}**{character.info.name}**{character.type.icon} - {character.ki.current} :fire:\n{kit}"
                    await self.ctx.send(actions)

                    if(self.turn == 1):  # manages the first turn possible actions
                        move = await choice.wait_for_choice(possible_action, all_character)
                        print(f"{move} : type {type(move)}")

                        if(type(move) == str):
                            if(move.lower() == "flee"):
                                return("flee")
                            
                            elif(move.lower() == "1"):
                                move_choice["move"] = "skip"
                                move_list.append(move_choice)
                                decision = True
                            
                            elif(move.lower() == "3"):
                                move_choice["move"] = 3
                                move_list.append(move_choice)
                                decision = True
                        
                        elif(type(move) == list):
                            if(move[0].lower() == "check" and move[1].isdigit()):  # manages the check option
                                index = int(move[1]) - 1
                                to_display = all_character[index]
                                displayer.character = to_display

                                await self.ctx.send(f"<@{self.player.id}> Here are some informations about {to_display.image.icon}**{to_display.info.name}**{to_display.type.icon} :")
                                await displayer.display(combat_format = True)
                                await asyncio.sleep(2)

                                decision = False
                    
                    else:  # turn > 1
                        move = await choice.wait_for_choice(possible_action, all_character)

                        if(type(move) == str):
                            if(move.isdigit()):  # convert the str to int
                                move = int(move)                    
                                
                                # basic choice
                                if(move > 0 and move <= 3):
                                    if(move == 1):  # sequence
                                        team_display = Team_displayer(team[0], team[1])
                                        targetable_team_a, targetable_team_b = await team_display.get_targetable("sequence")

                                        # allies
                                        if(len(targetable_team_a) > 0):
                                            target_display += "\n__Target__ : \n🔵 - Your team :\n"

                                            # retrieve all the targetable units
                                            unit_index = 1

                                            for ally in targetable_team_a:
                                                await asyncio.sleep(0)

                                                target_display += f"{unit_index}. {ally.image.icon}**{ally.info.name}**{ally.type.icon}\n"

                                                unit_index += 1
                                        
                                        # enemies
                                        if(len(targetable_team_b) > 0):
                                            target_display += "\n🔴 - Enemy team :\n" 

                                            # retrieve all the targetable enemies
                                            for enemy in targetable_team_b:
                                                await asyncio.sleep(0)

                                                target_display += f"{unit_index}. {enemy.image.icon}**{enemy.info.name}**{enemy.type.icon}\n"

                                                unit_index += 1
                                        
                                        # display the targets
                                        await self.ctx.send(f"<@{self.player.id}> Please select a target among the following for `Sequence 👊` :\n{target_display}")
                                        
                                        targetable = targetable_team_a + targetable_team_b
                                        target = await choice.wait_for_target(targetable)

                                        move_choice["move"], move_choice["target"] = move, target
                                        move_list.append(move_choice)
                                        decision = True
                                    
                                    elif(move == 2):
                                        move_choice["move"] = 2
                                        move_list.append(move_choice)
                                        decision = True
                                    
                                    elif(move == 3):
                                        move_choice["move"] = 3
                                        move_list.append(move_choice)
                                        decision = True

                                # ability choice
                                # now check if the chosen ability is possible
                                elif(move > 3 and move <= len(character.ability)+3):  
                                    # -4 because we start counting at 4
                                    # 4(choice) == first ability 
                                    ability = character.ability[move-4]

                                    # check if the ability needs a target
                                    need_target = ability.need_target

                                    # if the ability is not on cooldown
                                    if(ability.cooldown <= 0):  
                                        # check if the character has enough ki
                                        if(character.ki.current >= ability.cost):
                                            # check if it needs a target or not
                                            if(need_target):
                                                team_display = Team_displayer(team[0], team[1])
                                                targetable_team_a, targetable_team_b = await team_display.get_targetable("ability", ability = ability)

                                                # allies
                                                if(len(targetable_team_a) > 0):
                                                    target_display += "\n__Target__ : \n🔵 - Your team :\n"

                                                    # retrieve all the targetable units
                                                    unit_index = 1

                                                    for ally in targetable_team_a:
                                                        await asyncio.sleep(0)

                                                        target_display += f"{unit_index}. {ally.image.icon}**{ally.info.name}**{ally.type.icon}\n"

                                                        unit_index += 1
                                                
                                                # enemies
                                                if(len(targetable_team_b) > 0):
                                                    target_display += "\n🔴 - Enemy team :\n" 

                                                    # retrieve all the targetable enemies
                                                    for enemy in targetable_team_b:
                                                        await asyncio.sleep(0)

                                                        target_display += f"{unit_index}. {enemy.image.icon}**{enemy.info.name}**{enemy.type.icon}\n"

                                                        unit_index += 1

                                                # send the message 
                                                await self.ctx.send(f"<@{self.player.id}> Please select a target among the following for `{ability.name}`{ability.icon}` : \n{target_display}")
                                                
                                                # get all the targetable units
                                                targetable = targetable_team_a + targetable_team_b

                                                # wait for target
                                                target = await choice.wait_for_target(targetable)
                                                move_choice["move"], move_choice["target"] = move, target
                                                move_list.append(move_choice)
                                                decision = True

                                            else:  # doesn't need a target
                                                move_choice["move"] = move
                                                move_list.append(move_choice)
                                                decision = True
                                        
                                        else:
                                            decision = False
                                            await self.ctx.send(f"<@{self.player.id}> 🔥 ⚠ Not enough ki : {character.ki.current} / {ability.cost}")
                                            await asyncio.sleep(1)

                                    else:  # ability is on cooldown
                                        decision = False
                                        await self.ctx.send(f"<@{self.player.id}> ⏳ ⚠ Ability on cooldown : {ability.cooldown} turns.")
                                        await asyncio.sleep(1)

                    # end main while
            
            # end for character in team
            order += 1
        
        # end of method
        print(f"chosen move : {move_list}")
        return(move_list)