# utility.cog.Character

This directory manages the **Characters**.

# File

- `character.py` : Represents a character object.

- `getter.py` : Character's informations getter.

# Directory

- `/ability` : Manages the abilities, effects, passive, etc.

- `/attribute` : Character's attributes classes.

- `/list` : Character's list.

## How to add a character ?

First, create the character by creating a new file in `cog.character.list`.

Then, add the character into `getter.get_character()`.

Finally, add it to the banner (Basic, expansion, Muscle).

## Add it as opponent :

Go to `utility.cog.command._train` and add the chaarcter's id to the attribute `possible_opponent`
