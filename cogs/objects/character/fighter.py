'''
Manages the fighter object.

Last update: 28/05/19
'''

# Init

import asyncio

# Object

from cogs.objects.character.character import Character

class Fighter(Character):
    '''
    Represent a Fighter

    `character` : must be `Character/Enemy` object.

    Attributes :
        Basics :
        - info : Return character infos.

        Fight infos :
        - statut : Return the statut of the fighter (0 def, 1 attack)

        Effects :
        - buff : Return list of objects buff
        - debuff : Return list of objects debuff
        - dot : Return list of objects dot
    '''

    # Instance attributes

    def __init__(self, character):
        self.stat = character
        self.level = 0
        self.awakening = 0

        # Fight infos
        self.statut = 0  # 0 or 1 : 0 = defenser, 1 = attacker

        # Effects
        self.buff = []  # List of buff objects
        self.debuff = []  # List of debuff objects
        self.dot = []  # List of dot objects