'''
Display the informations about a character.

Last update: 09/06/19
'''

# Dependancies
import asyncio

# Utils

from cogs.utils.functions.readability.embed import Basic_embed
from cogs.utils.functions.translation.gettext_config import Translate

from cogs.objects.character.characters_list.all_char import Get_char

async def Display_character_info(client, ctx, character_id):
    '''
    `coroutine`

    Displays the information of the passed character. Displays its stats from lv.1 to 150
    and from N rarity to LR.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `character_id` : must be type `int` and represents a character id.

    Return: discord.Message (embed)
    '''

    # Init

    _ = await Translate(client, ctx)
    display = Basic_embed(client)
    kit = Basic_embed(client)

    char = await Get_char(character_id)
    char.level = 1
    char.rarity_value = 0
    await char.init(client, ctx)

    sec_char = await Get_char(character_id)
    sec_char.level = 150
    sec_char.rarity_value = 5
    await sec_char.init(client, ctx)

    # Managing the display

    kit_info = ''
    basic_info = _('__Name__ : {}\n__Saga__ : {}\n__Level__ : {} *({})*\n__Base rarity__ : {} ({})\n__Health__ : {:,} *({:,})* :hearts:\n__Physical damage__ : {:,} *({:,})* ⚔\n__Ki damage__ : {:,} *({:,})* 🏵\n__Armor__ : {:,} *({:,})* :shield:\n__Spirit__ : {:,} *({:,})* :rosette:\n').format(char.name, char.saga, 1, 150, char.rarity_icon, sec_char.rarity_icon, char.max_hp, sec_char.max_hp, char.physical_damage_max, sec_char.physical_damage_max, char.ki_damage_max, sec_char.ki_damage_max, char.physical_defense, sec_char.physical_defense, char.ki_defense, sec_char.ki_defense)
    
    for ability in char.ability_list:
        await asyncio.sleep(0)

        ability = ability()
        await ability.init(client, ctx, sec_char)
        
        kit_info += _('{}__{}__ : {}\n\n').format(ability.icon, ability.name, ability.description)

    display.add_field(name = _('{}\'s informations :').format(char.name), value = basic_info, inline = False)
    display.set_image(url = char.image)

    kit.add_field(name = _('{}\'s kit : ').format(char.name), value = kit_info, inline = False)

    await ctx.send(embed = display)
    await ctx.send(embed = kit)
    return