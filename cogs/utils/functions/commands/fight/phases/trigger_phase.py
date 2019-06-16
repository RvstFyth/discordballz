'''
Manages the trigger phase of the fight.

Last update: 15/06/19
'''

# Dependancies

import asyncio
from random import randint

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.readability.embed import Basic_embed

async def Triggers_phase(client, ctx, player, character_team, enemy_team, team_num):
    '''
    `coroutine`

    Trigger the characters effects.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `player` : must be `discord.Member` object.

    `character_team` : must be list of `Character` objects.

    `team_num` : must be type `int` : 0 = Player team, 1 = Enemy team.

    Return: discord.Message
    '''

    # Init

    _ = await Translate(client, ctx)

    character_count = 1

    # Character team
    team_effects = False
    char_effect = False
    team_triggers = ''
        
    # Calculating
        
    for character in character_team:
        await asyncio.sleep(0)
        
        # Trigger the death effects if they haven't been triggered
        '''
        for character in character_team:
            await asyncio.sleep(0)

            if(character.current_hp <= 0):  # If the char is dead
                if(character.being_killed_triggered == False):  # If his dead effect didn't trigger
                    await character.On_being_killed(character, character_team, enemy_team)
                    character.being_killed_triggered = True
        
        for enemy in enemy_team:
            await asyncio.sleep(0)

            if(enemy.current_hp <= 0):
                if(enemy.current_hp <= 0):  # If the char is dead
                    if(enemy.being_killed_triggered == False):  # If his dead effect didn't trigger
                        await enemy.On_being_killed(enemy, character_team, enemy_team)
                        enemy.being_killed_triggered = True'''

        # Reinit
        character_trigger = ''

        # Buff
        char_buff = False
        team_buff_display = _('\n__Effects__ : ')
        team_buff_stack_display = _('\n__Stack__ : ')
        team_buff_damage_display = _('\n__Healing__ : ')
        team_buff_duration_display = _('\n__Time remaining__ : ')
        
        # Debuff
        char_debuff = False
        team_debuff_display = _('\n__Effects__ : ')
        team_debuff_stack_display = _('\n__Stack__ : ')
        team_debuff_damage_display = _('\n__Damages__ : ')
        team_debuff_duration_display = _('\n__Time remaining__ : ')
        
        # Dot
        char_dot = False
        team_dot_display = _('\n__Effects__ : ') # List the character dots
        team_dot_stack_display = _('\n__Stack__ : ')
        team_dot_damage_display = _('\n__Damages__ : ')
        team_dot_duration_display = _('\n__Time remaining__ : ')
            
        # Effects
        # If there is any effects, we display it
        
        char_effect = False

        # Effects
        # Buff
        if(character.current_hp > 0):  # Only check if the character is still alive
            if(len(character.buff) > 0):
                for buff in character.buff : 
                    await asyncio.sleep(0)

                    # Check if the effect is active
                    if buff.duration <= 0:
                        character.buff.remove(buff)  # The effect is, over, removing it

                        if(len(character.buff) == 0):
                            break  # No more buff to check, we go out of the loop
                    
                    else:
                        buff_damage_done = await buff.apply(character, character_team, enemy_team)  # Apply the buff's effects

                        # Duration
                        buff.duration -= 1

                        team_effects = True
                        char_effect = True
                        char_buff = True

                        # Set buff display
                        team_buff_display += '`{}`{} | '.format(buff.name, buff.icon)
                        team_buff_stack_display += '**{}** | '.format(buff.stack)
                        team_buff_damage_display += '+ **{}**:hearts: | '.format(buff_damage_done)
                        team_buff_duration_display += '**{}** | '.format(buff.duration)
            
            if(char_buff):  # If the character has a buff we display it
                character_trigger += _('\n------------ Buffs ------------')
                character_trigger += team_buff_display
                character_trigger += team_buff_stack_display
                character_trigger += team_buff_damage_display
                character_trigger += team_buff_duration_display
                character_trigger += '\n'
            
            # Debuff
            if(len(character.debuff) > 0):
                for debuff in character.debuff :
                    await asyncio.sleep(0)

                    # Check if the effect is active or not
                    if debuff.duration <= 0:
                        character.debuff.remove(debuff) 

                        if(len(character.debuff) == 0):
                            break
                    
                    else:
                        debuff_damage_done = await debuff.apply(character, character_team, enemy_team)

                        # Duration
                        debuff.duration -= 1

                        team_effects = True
                        char_effect = True
                        char_debuff = True

                        # Set debuff display
                        team_debuff_display += '`{}`{} | '.format(debuff.name, debuff.icon)
                        team_debuff_stack_display += '**{}** | '.format(debuff.stack)
                        team_debuff_damage_display += '- **{}** | '.format(debuff_damage_done)
                        team_debuff_duration_display += '**{}** | '.format(debuff.duration)
            
            if(char_debuff):  # If character has a debuff we display it
                character_trigger += _('\n------------ Debuffs ------------')
                character_trigger += team_debuff_display
                character_trigger += team_debuff_stack_display
                character_trigger += team_debuff_damage_display
                character_trigger += team_debuff_duration_display
                character_trigger += '\n'

            # Dot
            if(len(character.dot) > 0):
                for dot in character.dot :
                    await asyncio.sleep(0)

                    # If one of the effect is over
                    if(dot.duration <= 0):
                        character.dot.remove(dot)

                        if(len(character.dot) == 0):  # If the character has no dot, we go out of the loop
                            break
                    
                    else:
                    
                        # Duration
                        dot_damage_done = await dot.apply(character, character_team, enemy_team)
                        dot.duration -= 1

                        # If the effect is not over, apply the effect

                        team_effects = True
                        char_effect = True 
                        char_dot = True

                        # The character has a dot on him, we display
                        team_dot_display += '`{}`{} | '.format(dot.name, dot.icon)
                        team_dot_stack_display += '**{}** | '.format(dot.stack)
                        team_dot_damage_display += '- **{}** | '.format(dot_damage_done)
                        team_dot_duration_display += '**{}** | '.format(dot.duration)
            
            if(char_dot):  # if character has a dot we display it
                character_trigger += _('\n------------ Damages over time ------------')
                character_trigger += team_dot_display
                character_trigger += team_dot_stack_display
                character_trigger += team_dot_damage_display
                character_trigger += team_dot_duration_display
                character_trigger += '\n'
            
            # Regens
            # Ki   
            if(character.flag == 0):  # If character is attacking
                character.current_ki += character.ki_regen + randint(1, 5) # Apply the ki regen
            
            if(character.flag == 1):  # If character is charging we don't do anything as it gains ki while battle phase
                pass
            
            if(character.flag == 2):  # If defending
                character.current_ki += character.ki_regen
            
            if(character.flag == 3):  # If stunned, doesn't gain anything
                pass

            if(character.current_ki > character.max_ki):  # If the ki regen is over the max, we set to max
                character.current_ki = character.max_ki
            
            # Health

            if(character.current_hp > 0):
                character.current_hp += character.health_regen

                if(character.current_hp > character.max_hp):
                    character.current_hp = character.max_hp
            
            # Display character name

            if(char_effect):
                team_triggers += '\n#{} - **{}**{}{} :{}'.format(character_count, character.name, character.rarity_icon, character.type_icon, character_trigger)

        character_count += 1

    ### END CALCULATION ###

    # End check effects for team
    # Display

    if team_effects:
        if(team_num == 0):
            final_display = _('🔵 - {}\'s Team :').format(player.name) + team_triggers + '\n'
        
        elif(team_num == 1):
            final_display = _('🔴 - Enemy Team :').format(player.name) + team_triggers + '\n'

        # Send
        await ctx.send(final_display)