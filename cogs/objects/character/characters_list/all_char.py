'''
Return the correct character object in function of the global id passed.

Last update: 26/05/19
'''

# Dependancies

import asyncio

async def Get_char(char_id):
    '''
    `coroutine`

    Return the character object of the passed global id.

    `char_id` : must be type `int` and represent a global id.

    Return: `Character` object.
    '''

    if(char_id == 1):
        
        # Import the character

        from cogs.objects.character.characters_list.char_1 import Char_1

        char_ = Char_1()

        return(char_)