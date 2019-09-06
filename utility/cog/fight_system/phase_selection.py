"""
Manages the selection phase.

--

Author : DrLarck

Last update : 06/09/19 (DrLarck)
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

        # define the bot's team
        if(player_team == 0):
            bot_team = team[0]
            bot_enemy = team[1]
        
        elif(player_team == 1):
            bot_team = team[1]
            bot_enemy = team[0]
    
        player_team = team[player_team]
        
        possible_action = []  # list of possible actions (str)
        all_character = team[0]+team[1]
        order = 1
        
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

            if(character != None):
                if(character.health.current > 0 and character.posture.stunned == False):
                    if(character.is_npc == False):
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
                            
                            if(len(character.ability) > 0):  # if the character has an ability
                                # init
                                kit += "\n\n__Abilities__ :\n\n"
                                ability_index = 4

                                for ability in character.ability:
                                    await asyncio.sleep(0)

                                    ability = ability(
                                        self.client,
                                        self.ctx,
                                        None,
                                        None,
                                        None,
                                        None
                                    )

                                    # add a new possible action
                                    possible_action.append(str(ability_index))

                                    kit += f"`{ability_index}. {ability.name}`{ability.icon} (:fire: {ability.cost} / {character.ki.current})\n"
                                    ability_index += 1
                            
                            else:
                                kit += "\n"
                        
                        kit += f"\nTo **flee** the fight, type `flee`, to **take a look at** a specific unit, type `check [unit index]`."
                        
                        # ask for the player's action
                        decision = False

                        # main loop
                        while(decision == False):
                            await asyncio.sleep(0)

                            # init
                            target_display = ""
                            unit_index = 1

                            # display the actions
                            actions = f"<@{self.player.id}> Please select an action amoung the following for #{order} {character.image.icon}**{character.info.name}**{character.type.icon} - {character.ki.current} :fire:\n{kit}"
                            await self.ctx.send(actions)

                            if(self.turn == 1):  # manages the first turn possible actions
                                move = await choice.wait_for_choice(possible_action, all_character)

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
                                    if(move.lower() == "flee"):
                                        return("flee")

                                    if(move.isdigit()):  # convert the str to int
                                        move = int(move)                    
                                        
                                        # basic choice
                                        if(move > 0 and move <= 3):
                                            if(move == 1):  # sequence
                                                team_display = Team_displayer(self.client, self.ctx, self.player, team[0], team[1])
                                                targetable_team_a, targetable_team_b = await team_display.get_targetable("sequence")

                                                # allies
                                                if(len(targetable_team_a) > 0):
                                                    target_display += "\n__Target__ : \n🔵 - Your team :\n"

                                                    # retrieve all the targetable units
                                                    unit_index = 1
                                                    display_targetable, unit_index = await self.display_targetable(targetable_team_a, unit_index)
                                                    target_display += display_targetable
                                                
                                                # enemies
                                                if(len(targetable_team_b) > 0):
                                                    target_display += "\n🔴 - Enemy team :\n" 

                                                    # retrieve all the targetable enemies
                                                    display_targetable, unit_index = await self.display_targetable(targetable_team_b, unit_index)
                                                    target_display += display_targetable
                                                
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
                                            ability = ability(
                                                self.client,
                                                self.ctx,
                                                None,
                                                None,
                                                None,
                                                None
                                            )

                                            # check if the ability needs a target
                                            need_target = ability.need_target

                                            # if the ability is not on cooldown
                                            if(ability.cooldown <= 0):  
                                                # check if the character has enough ki
                                                if(character.ki.current >= ability.cost):
                                                    # check if it needs a target or not
                                                    if(need_target):
                                                        team_display = Team_displayer(self.client, self.ctx, self.player, team[0], team[1])
                                                        targetable_team_a, targetable_team_b = await team_display.get_targetable("ability", ability = ability)

                                                        # allies
                                                        if(len(targetable_team_a) > 0):
                                                            target_display += "\n__Target__ : \n🔵 - Your team :\n"

                                                            # retrieve all the targetable units
                                                            unit_index = 1

                                                            display_targetable, unit_index = await self.display_targetable(targetable_team_a, unit_index)
                                                            target_display += display_targetable
                                                        
                                                        # enemies
                                                        if(len(targetable_team_b) > 0):
                                                            target_display += "\n🔴 - Enemy team :\n" 

                                                            # retrieve all the targetable enemies
                                                            display_targetable, unit_index = await self.display_targetable(targetable_team_b, unit_index)
                                                            target_display += display_targetable

                                                        # send the message 
                                                        await self.ctx.send(f"<@{self.player.id}> Please select a target among the following for `{ability.name}`{ability.icon} : \n{target_display}")
                                                        
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

                                elif(type(move) == list):
                                    if(move[0].lower() == "check" and move[1].isdigit()):  # manages the check option
                                        index = int(move[1]) - 1
                                        to_display = all_character[index]
                                        displayer.character = to_display

                                        await self.ctx.send(f"<@{self.player.id}> Here are some informations about {to_display.image.icon}**{to_display.info.name}**{to_display.type.icon} :")
                                        await displayer.display(combat_format = True)
                                        await asyncio.sleep(2)

                                        decision = False

                    else:  # the character is a bot
                        bot_move = await character.bot(self.client, self.ctx, self.player, bot_team, bot_enemy, self.turn)

                        move_list.append(bot_move)

                    # end main while
                
                    # end for character in team
                    order += 1
                
                else:  # the character is dead or cannot play the turn
                    move_list.append(None)
        
        # end of method
        return(move_list)
    
    async def display_targetable(self, _list, unit_index):
        """
        `coroutine`
        
        Return the display of the targetables units in the list.

        - Parameter : 

        `_list` : List of targetable units to display.

        `unit_index` : The index to count with.

        --

        Return : str, int
        """

        # init
        target_display = ""

        for unit in _list:
            await asyncio.sleep(0)

            # get the posture
            posture, posture_icon = await unit.posture.get_posture()

            target_display += f"{unit_index}. {unit.image.icon}**{unit.info.name}**{unit.type.icon} - **{unit.health.current:,}** :hearts: : {posture}{posture_icon}\n"
            
            # get the ally's bonus
            if(len(unit.bonus) > 0):
                target_display += f"__Bonus__ : "
                bonus_index = 0

                for bonus in unit.bonus:
                    await asyncio.sleep(0)
                    
                    if(bonus_index == 0):
                        target_display += f"{bonus.icon}[{bonus.stack}|{bonus.duration}]"
                    
                    else:
                        target_display += f", {bonus.icon}[{bonus.stack}|{bonus.duration}]"

                    bonus_index += 1
                
                target_display += "\n"
            
            # get the ally's malus
            if(len(unit.malus) > 0):
                target_display += f"__Malus__ : "
                malus_index = 0

                for malus in unit.malus:
                    await asyncio.sleep(0)
                    
                    if(malus_index == 0):
                        target_display += f"{malus.icon}[{malus.stack}|{malus.duration}]"
                    
                    else:
                        target_display += f", {malus.icon}[{malus.stack}|{malus.duration}]"

                    malus_index += 1
                
                target_display += "\n"

            unit_index += 1
        
        return(target_display, unit_index)