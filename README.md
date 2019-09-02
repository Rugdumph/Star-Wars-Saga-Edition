# Star-Wars-Saga-Edition

This project is turning the Star Wars Roleplaying Game into code. To be used mainly as an aid to game-masters. More information on the game can be found at: https://en.wikipedia.org/wiki/Star_Wars_Roleplaying_Game_(Wizards_of_the_Coast)
At this point it does very little. You can create and load level 1 characters.

* * *
Usage: 
Run gui.py

* * *
Features

+ Create a heroic character
+ Save/Load character

* * *
Planned Additions

+ Add/finish leveling (requires finishing features/talents/force powers)
+ Add features
+ Add talents
+ Add force powers
+ Add beast character creation
+ Add non-heroic character creation
+ Add items (weapons/armor/usables)
+ Add battle/encounter manager

* * *
Files

battle.py - (INCOMPLETE) Battle/encounter manager.
Will be used to track turns, HP, and character during encounter. Hopefully one day do more like calculate damage, allow usage of features/talents. Take 'cover' and position into calculations.

beast_character.py - (NOT-STARTED) Will be used to create/level beasts.

character.py - Contains the backbone of all characters (Heroic/Non-heroic/Beasts). Contains stats (like HP/abilities/ect). 

gui.py - (WORK IN PROGRESS) Contains mostly GUI but also some logic. Like when a level will require ability to increment. Entry point to program at this point.

heroic_character.py - Contains leveling methods for heroic classes/characters.

mechanics.py - (INCOMPLETE) Contains miscellaneous functions. Like dice rolls. Will contains functions for reading the CSV files.

nonheroic_character.py - (NOT-STARTED) Will be used to create/level non-heroic characters.

***
Flies (CSV)

features.csv - Contains information on all the features

skills.csv - Contains information on all the skills

species.csv - Contains information on all the species
