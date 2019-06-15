'''
Return the correct character object in function of the global id passed.

Last update: 15/06/19
'''

# Dependancies

import asyncio

async def Get_char(char_id):
    '''
    `coroutine`

    Return the character object of the passed global id.

    `char_id` : must be type `int` and represent a global id.

    Return: `Character` object, if not found return None.
    '''

    if(char_id == 1):
        
        # Import the character

        from cogs.objects.character.characters_list.char_1 import Char_1

        char_ = Char_1()

        return(char_)
    
    if(char_id == 2):

        from cogs.objects.character.characters_list.char_2 import Char_2

        char_ = Char_2()

        return(char_)

    else:
        return