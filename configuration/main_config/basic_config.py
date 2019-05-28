'''
Manages the basic configuration for the program. Such as the prefixes, the cogs, the version, etc.

Last update: 27/05/19
'''

# Dependancies

import os

# Bot Token

BOT_TOKEN = os.environ['BOT_TOKEN']

# Prefix

PREFIX = ['Db', 'db', 'D!', 'd!']

# Version control
# The 'build' value is only applied for under 'release' phases
# Any file update increases the V_MIN value by 1 (or V_BUILD value if it's active)
# Only one increase per file

V_MAJ,V_MED,V_MIN,V_BUILD,V_PHASE = 3,0,0,215, 'Prototype'

# Cogs
# To add a cog, type the path to the cog as a string (do not use `/`, it's represented by `.`)
# Allow 3 cog per line

COGS = ['cogs.commands.summon', 'cogs.commands.start', 'cogs.commands.profile',
        'cogs.commands.fight', 'cogs.event.on_ready']