import random
from mechanics import *
from character import *
from operator import itemgetter

class Combatant(Person):
	def __init__(self, character, flat_footed):
		self.current_HP = character.max_HP

		# Action counts
		self.swift_action = 0
		self.move_action = 0
		self.standard_action = 0

		# Set given attributes
		self.flat_footed = flat_footed

		# Set battle stats to defaults 
		self.alive = True
		self.condition = 0	# 0 being normal and -5 unconscious

		# Store threshold to reduces number of calls to the person class
		self.threshold = self.get_threshold()



	def set_HP(new_HP):
		self.current_HP = new_HP


	def take_damage(damage):
		# If already dead, return False
		if not self.is_alvie:
			return False
		# Else if unconscious and damage exceeds threshold, 
		# insta-death (reduce HP to 0) and return True.
		elif not self.is_conscious() and damage >= self.threshold:
			self.current_HP = 0
			return True
		# Else just deduct health and reduce condition if 
		# needed and return True
		else
			self.current_HP -= damage
			if damage >= self.threshold:
				self.condition -= 1
			return True


	def attack_hit(defense_type, attack_score):
		if defense_type is 'reflex_def':
			return self.get_refl_def() =< attack_score
		elif defense_type is 'fortitude_def':
			return self.get_fort_def() =< attack_score
		elif defense_type is 'will_def':
			return self.get_will_def() =< attack_score


	def heal(amount):
		# If alive, add health upto max health point level, but not past.
		if self.is_alvie():
			self.current_HP = min(amount + self.current_HP, self.max_HP)
			return True
		else:
			return False


	def is_conscious():
		return self.condition > -5


	def is_alvie():
		return self.current_HP > 0


	def new_turn():
		self.swift_action = 1
		self.move_action = 1
		self.standard_action = 1


class Battle():
	def __init__(self):
		self.participants = list()
		self.turn_order = list()
		self.battle_started = False

		self.move_number = 0 	# Used with % to determine turn


	def add_participant(participant, init_roll):
		if self.battle_started:
			init = participant.skill_check(skill, init_roll, 0)
			self.participants.append((participant, init))
			return True
		else:
			return False

	def start_battle():
		if self.battle_started is True:
			return False
		else:
			self.participants.sort(key=itemgetter(1))
			self.battle_started = True

	def next_turn():
		next_combatant = participants[move_number%len(participants)]
		move_number += 1
		return next_combatant
