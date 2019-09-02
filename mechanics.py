import random

def roll(sides):
	return random.randint(1, sides)


def abilitiesRoll():
	abilityScores = list()

	for i in range(0,6):	
	    # roll Abilities
	    abilityRoll = list()
	    for x in range(4):
	    	abilityRoll.append(roll(6))


		# get the sum of the highest three rolls
	    abilityRoll.sort()
	    abilitySum = 0
	    for x in range(1,4):
	        abilitySum += abilityRoll[x]

	    abilityScores.append(abilitySum)

	abilityScores.sort()
	return abilityScores