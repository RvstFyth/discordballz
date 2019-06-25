'''
Return certain class

Last update: 23/06/19
'''

# classes

# Abilities effect



async def Get_class(class_id: int):
    '''
    `coroutine`

    Return the class, not an instance of class.

    List :
    1. Acid
    2. Unity is strenght
    3. 
    '''

    if class_id == 1:
        from cogs.objects.character.abilities_effects.damages_over_time.acid import Acid
        return(Acid)
    
    if class_id == 2:
        from cogs.objects.character.abilities_effects.buff.unity_is_strenght import Unity_is_strenght
        return(Unity_is_strenght)
    
    else:
        print('Class not found.')
        return(None)