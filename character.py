from mechanics import *

class Character():
    def __init__(self, name, owner, species, abilities):
        # set name
        self.name = name    # Name of character
        self.owner = owner  # Name of real-world character owner

        # set abilities
        self.stre = abilities[0]
        self.dex  = abilities[1]
        self.con  = abilities[2]
        self.inte = abilities[3]
        self.wis  = abilities[4]
        self.cha  = abilities[5]

        # character stats
        self.base_attack = 0
        self.max_HP = 0
        self.speed = 0
        self.force_points = 0
        self.destiny_points = 0
        self.dark_side_score = 0

        # set character and class levels
        self.level = 0
        self.jedi_level = 0
        self.noble_level = 0
        self.scoundrel_level = 0
        self.scout_level = 0
        self.soldier = 0

        # set class defense bonuses
        self.class_reflex_def = 0
        self.class_fortitude_def = 0
        self.class_will_def = 0

        # set up feat/skill/talent lists
        self.char_feats = list()
        self.char_talents = list()
        self.trained_skills = list()
        self.focused_skills = list()


        # Leveling variables
        self.latest_class = None   # Used for talent/feat/skill selections
        self.unassigned_abil = 0   # Used to determine all abilities assigned
        self.total_skills = 0      # Used to determine all skills assigned
        self.total_talents = 0     # Used to determine all talents assigned
        self.total_feats = 0       # Used to determine all features assigned

        # Money, money, money 
        self.credits = 0

        # set species and add species bonuses ###### set species and add species bonuses ###### set species and add species bonuses #####

    def print_character_sheet(self):
        print("Name:", self.name)
        print("Level:", self.level)
        print("Species:", self.species)
        print("Str:", self.stre, (int)(self.stre/2)-5)
        print("Dex:", self.dex,  (int)(self.dex/2)-5)
        print("Con:", self.con,  (int)(self.con/2)-5)
        print("Int:", self.inte, (int)(self.inte/2)-5)
        print("Wis:", self.wis,  (int)(self.wis/2)-5)
        print("Cha:", self.cha,  (int)(self.cha/2)-5)
        print("Class Reflex Def", self.class_reflex_def)
        print("Class Fortitude Def", self.class_fortitude_def)
        print("Class Will Def", self.class_will_def)
        print("Credits:", self.credits)

    def character_sheet(self):
        myString = "Name: " + self.name \
        + "\n" +   "Level: " + str(self.level) \
        + "\n" +   "Species: " + self.species \
        + "\n" +   "Str: " + str(self.stre) \
        + "\n" +   "Dex: " + str(self.dex) \
        + "\n" +   "Con: " + str(self.con) \
        + "\n" +   "Inte: " + str(self.inte) \
        + "\n" +   "Wis: " + str(self.wis) \
        + "\n" +   "Cha: " + str(self.cha) \
        + "\n" +   "Class Reflex Def: " + str(self.class_reflex_def) \
        + "\n" +   "Class Fortitude Def: " + str(self.class_fortitude_def) \
        + "\n" +   "Class Will Def: " + str(self.class_will_def) \
        + "\n" +   "Credits: " + str(self.credits)

        return myString


# # #
# # # # # #
# # # # # # # # # # #
# Expertise Methods # # *
# # # # # # # # # # #
# # # # # #
# # #


# # # # # 
# Requirement Tests
# # # # # 
    def check_skill_req(req_skills):
        return req_skills in self.trained_skills

    def check_talent_req(req_talents):
        return req_talents in self.char_talents

    def check_ability_req(req_abilities):
        # Return true if ability requirement is 'None' or if ability is high
        # enough.
        return  (req_skills[0] is 'None' or self.stre <= int(req_skills[0]))\
            and (req_skills[0] is 'None' or self.dex <= int(req_skills[0]))\
            and (req_skills[0] is 'None' or self.con <= int(req_skills[0]))\
            and (req_skills[0] is 'None' or self.inte <= int(req_skills[0]))\
            and (req_skills[0] is 'None' or self.wis <= int(req_skills[0]))\
            and (req_skills[0] is 'None' or self.cha <= int(req_skills[0]))

    def check_species_req(req_species):
        if req_species is 'All':
            return True

        # Deal with 'non-droids' ############### Deal with 'non-droids' ############### Deal with 'non-droids' ##################
        # Deal with 'Rage' species ######### Deal with 'Rage' species ######### Deal with 'Rage' species ########
        # Deal with size constants ######### Deal with size constants ######### Deal with size constants ########
        return False

    def check_base_attach(req_base_att):
        return int(req_base_att) <= self.base_attack


# # # # # 
# Add Talents
# # # # # 
    def add_talent(talent):
        # Add requirement check ######## Add requirement check ######## Add requirement check #######
        if talent in self.char_talents:
            return False
        else:
            self.char_talents.append(talent)


# # # # # 
# Add Skills
# # # # # 
    def add_skill(skill):
        # Add requirement check ######## Add requirement check ######## Add requirement check #######
        if skill in self.trained_skills:
            return False
        else:
            self.trained_skills.append(skill)
            return True

# # # # # 
# Add Features
# # # # # 
    def add_feature(feature):
        # Add requirement check ######## Add requirement check ######## Add requirement check #######
        if feature in self.char_feats:
            return False
        else:
            self.char_feats.append(feature)
            return True



# # #
# # # # # #
# # # # # # # # # #
# Getters   # # # # # # *
# # # # # # # # # #
# # # # # #
# # #

# # # # # 
# Ability Modifiers
# # # # # 

    def stre_mod(self):
        return int((self.stre/2)-5) 

    def dex_mod(self):
        return int((self.dex/2)-5) 

    def con_mod(self):
        return int((self.con/2)-5) 

    def inte_mod(self):
        return int((self.inte/2)-5) 

    def wis_mod(self):
        return int((self.wis/2)-5) 

    def cha_mod(self):
        return int((self.cha/2)-5)


    def get_mod(self, ability):
        if ability is 'Stre':
            return stre_mod()
        elif ability is 'Dex':
            return dex_mod()
        elif ability is 'Con':
            return con_mod()
        elif ability is 'Inte':
            return inte_mod()
        elif ability is 'Wis':
            return wis_mod()
        elif ability is 'Cha':
            return cha_mod()
        else:
            return None

# # # # # 
# Skill Bonuses
# # # # # 
    def get_skill_bonus(skill_info):
        skill_bonus = int(self.level/2)

        # Add skill focus bonus
        if skill_info[0] in self.focused_skills:
            skill_bonus += 5

        # Add Ability Modifier
        skill_bonus += get_mod(skill_info[1])

        # Add Feat Bonuses  ####### Add Feat Bonuses  ####### Add Feat Bonuses  ####### Add Feat Bonuses  ######
        # Add Trait Bonuses ####### Add Trait Bonuses ####### Add Trait Bonuses ####### Add Trait Bonuses ######
        # Add Skill Bonuses ####### Add Skill Bonuses ####### Add Skill Bonuses ####### Add Skill Bonuses ######
        # Add Equipment Bonuses ####### Add Equipment Bonuses ####### Add Equipment Bonuses ######

        return skill



# # # # # 
# Defenses/Threshold
# # # # # 
    def get_refl_def(self):
        refl_def = 10 + self.level + dex_mod() + self.class_reflex_def

        # Add size modifier
        if self.size is "Colossal":
            refl_def += -10
        elif self.size is "Gargantuan":
            refl_def += -5
        elif self.size is "Huge":
            refl_def += -2
        elif self.size is "Large":
            refl_def += -1
        elif self.size is "Medium":
            pass
        elif self.size is "Small":
            refl_def += 1
        elif self.size is "Tiny":
            refl_def += 2
        elif self.size is "Diminutive":
            refl_def += 5
        elif self.size is "Fine":
            refl_def += 10
        # Add "or armor" to calculation ######## Add "or armor" to calculation ######## Add "or armor" to calculation #######
        return refl_def


    def get_fort_def(self):
        fort_def = 10 + self.level + con_mod() + self.class_fortitude_def
        # Add "equipment bonus" to calculation ######## Add "equipment bonus" to calculation ######## Add "equipment bonus" to calculation #######
        return fort_def


    def get_will_def(self):
        return 10 + self.level + wis_mod() + self.class_will_def


    def get_threshold(self):
        if self.size is "Colossal":
            return self.fort_def() + 50
        elif self.size is "Gargantuan":
            return self.fort_def() + 20
        elif self.size is "Huge":
            return self.fort_def() + 10
        elif self.size is "Large":
            return self.fort_def() + 5

    def remaining_talents(self):
        return self.total_talents - len(self.char_talents)

    def remaining_skills(self):
        return self.total_skills - len(self.trained_skills)

    def remaining_features(self):
        return self.total_feats - len(self.char_feats)


# # #
# # # # # #
# # # # # # # # # #
# Skill Checks  # # # # *
# # # # # # # # # #
# # # # # #
# # #

    def skill_check(skill, d20_roll, untrained_penalty):
        skill_total = d20_roll

        # Add focus bonus or add untrained penalty as needed
        if skill in self.focused_skills:
            skill_total += 5
        elif skill not in self.trained_skills:
            skill_total -= untrained_penalty

        # Add level bonus
        skill_total += int(self.level/2)

# Replace with reading data from skills.csv
        # Add Ability modifier
        ## Skills with Dex as the key ability
        if skill in ['Acrobatics', 'Initiative', 'Pilot', 'Ride', 'Stealth']:
            skill_total += self.dex_mod()

        ## Skills with Stre as the key ability
        elif skill in ['Climb', 'Jump', 'Swim']:
            skill_total += self.stre_mod()

        ## Skills with Cha as the key ability
        elif skill in ['Deception', 'Gather Information', 'Persuasion', \
                          'Use the Force']:
            skill_total += self.cha_mod()

        ## Skill with Con as the key ability
        elif skill is 'Endurance':
            skill_total += self.con_mod()

        ## Skills with Int as the key ability
        elif skill in ['Knowledge (Bureaucracy)', \
                'Knowledge (Galactic lore)', 'Knowledge (Life sciences)', \
                'Knowledge (Physical sciences)', 'Knowledge (Social sciences)',\
                'Knowledge (Tactics)', 'Knowledge (Technology)', 'Mechanics', \
                'Use Computer']:
            skill_total += self.inte_mod()

        ## Skills with Wis as the key ability
        elif skill in ['Perception', 'Survival', 'Treat Injury']:
            skill_total += self.wis_mod()
# End replacement

        return skill_total