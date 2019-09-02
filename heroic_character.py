from character import *

class HeroicCharacter(Character):
    def __init__(self, name, owner, species, abilities):
        Character.__init__(self, name, owner, species, abilities)

        # Finish init ###### Finish init ###### Finish init ###### Finish init #####



# # #
# # # # # #
# # # # # # # # # #
# Leveling Methods  # *
# # # # # # # # # #
# # # # # #
# # #

# # # # # 
# Main leveling method, calls all other methods as needed
# # # # # 
    def level_up(self, char_class):

        # Test if ready to level up
        if self.level == 20:
            return False
        elif self.remaining_talents() != 0:
            return False
        elif self.remaining_skills() != 0:
            return False
        elif self.remaining_features() !=0:
            return False

        self.latest_class = char_class

        # Add character level 
        self.level += 1

        # Reset force points, increment destiny points
        self.destiny_points += 1
        self.force_points = 5 + int(self.level/2)

        # Determine class to level
        if char_class == "Jedi":
            self.level_jedi()
        elif char_class == "Noble":
            self.level_noble()
        elif char_class == "Scout":
            self.level_scout()
        elif char_class == "Scoundrel":
            self.level_scoundrel()
        elif char_class == "Soldier":
            self.level_soldier()

        # Add character level feats
        if ((self.level % 3) == 0) or self.level==1:
            self.total_feats += 1

        # Add ability increase
        if (self.level % 4) == 0:
            self.unassigned_abilities += 2

# # # # # 
# Level up as a Jedi
# # # # # 
    def level_jedi(self):
        self.jedi_level += 1

        if self.jedi_level == 1:
            # Increase hit points
            self.max_HP += 30 + self.con_mod()
            
            # Increase amount of skills
            self.total_skills += 2 + self.inte_mod()

            # Upgrade class defenses, keeping the highest defense 
            self.class_reflex_def = max(self.class_reflex_def, 1)
            self.class_fortitude_def = max(self.class_fortitude_def, 1)
            self.class_will_def = max(self.class_will_def, 1)
            
            # Add starting feats ########## Add starting feats ########## Add starting feats ########## Add starting feats ########## Add starting feats #########

            # Add to base attack
            self.base_attack += 1

            # Add starting credits
            if self.level == 1:
                self.credits = (roll(4) + roll(4) + roll(4)) * 100

        else:
            self.max_HP += roll(10) + self.con_mod()

            if self.jedi_level%2 == 0:
                self.total_feats += 1

            elif self.jedi_level%2 == 1:
                self.total_talents += 1

            # Add to base attack
            self.base_attack += 1

            # Add additional level bonuses


# # # # # 
# Level up as a Noble
# # # # # 
    def level_noble(self):
        self.noble_level += 1

        if self.noble_level == 1:
            # Increase hit points
            self.max_HP += 18 + self.con_mod()

            # Increase amount of skills
            self.total_skills += 6 + self.inte_mod()

            # Upgrade class defenses, keeping the highest defense 
            self.class_reflex_def = max(self.class_reflex_def, 1)
            self.class_will_def = max(self.class_will_def, 2)

            # Add starting feats ########## Add starting feats ########## Add starting feats ########## Add starting feats ########## Add starting feats #########


            # Add starting credits
            if self.level == 1:
                self.credits = (roll(4) + roll(4) + roll(4)) * 400

        else:
            self.max_HP += roll(6) + self.con_mod()


            if self.noble_level%2 == 0:
                self.total_feats += 1

            elif self.noble_level%2 == 1:
                self.total_talents += 1

            # Add to base attack
            self.base_attack += 1

            # Add additional level bonuses


# # # # # 
# level up as a Scoundrel
# # # # # 
    def level_scoundrel(self):
        self.scoundrel_level += 1

        if self.scoundrel_level == 1:
            # Increase hit points
            self.max_HP += 18 + self.con_mod()

            # Increase amount of skills
            self.total_skills += 4 + self.inte_mod()

            # Upgrade class defenses, keeping the highest defense 
            self.class_reflex_def = max(self.class_reflex_def, 2)
            self.class_will_def = max(self.class_will_def, 1)

            # Add starting feats ########## Add starting feats ########## Add starting feats ########## Add starting feats ########## Add starting feats ##########


            # Add starting credits
            if self.level == 1:
                self.credits = (roll(4) + roll(4) + roll(4)) * 250

        else:
            self.max_HP += roll(6) + self.con_mod()

            if self.scoundrel_level%2 == 0:
                self.total_feats += 1

            elif self.scoundrel_level%2 == 1:
                self.total_talents += 1

            if self.scoundrel_level%4 != 1:
                 # Add to base attack
                self.base_attack += 1               
            # Add additional level bonuses



# # # # # 
# Level up as a Scout
# # # # # 
    def level_scout(self):
        self.scout_level += 1

        if self.scout_level == 1:
            # Increase hit points
            self.max_HP += 24 + self.con_mod()

            # Increase amount of skills
            self.total_skills += 5 + self.inte_mod()

            # Upgrade class defenses, keeping the highest defense 
            self.class_reflex_def = max(self.class_reflex_def, 2)
            self.class_fortitude_def = max(self.class_fortitude_def, 1)

            # Add starting feats ########## Add starting feats ########## Add starting feats ########## Add starting feats ########## Add starting feats #########


            # Add starting credits
            if self.level == 1:
                self.credits = (roll(4) + roll(4) + roll(4)) * 250

        else:
            self.max_HP += roll(8) + self.con_mod()

            if self.scout_level%2 == 0:
                self.total_feats += 1

            elif self.scout_level%2 == 1:
                self.total_talents += 1

            if self.scout_level%4 != 1:
                 # Add to base attack
                self.base_attack += 1
            # Add additional level bonuses




# # # # # 
# Level up as a Soldier
# # # # # 
    def level_soldier(self):
        self.soldier_level += 1

        # If first level as a soldier
        if self.soldier_level == 1:
            # Increase hit points
            self.max_HP += 30 + self.con_mod()

            # Increase amount of skills
            self.total_skills += 3 + self.inte_mod()

            # Upgrade class defenses, keeping the highest defense 
            self.class_reflex_def = max(self.class_reflex_def, 1)
            self.class_fortitude_def = max(self.class_fortitude_def, 2)

            # Add starting feats ########## Add starting feats ########## Add starting feats ########## Add starting feats ########## Add starting feats ##########


            # Add to base attack
            self.base_attack += 1

            # Add starting credits
            if self.level == 1:
                self.credits = (roll(4) + roll(4) + roll(4)) * 250

        # If not first level as a soldier
        else:
            self.max_HP += roll(10) + self.con_mod()

            if self.soldier_level%2 == 0:
                self.total_feats += 1

            elif self.soldier_level%2 == 1:
                self.total_talents += 1

            # Add to base attack
            self.base_attack += 1
            # Add additional level bonuses

# # #
# # # # # #
# # # # # # # # # #
# Other/MISC  # # # # *
# # # # # # # # # #
# # # # # #
# # #
    
    def use_force_point(self):
        if self.force_points > 0:
            self.force_points -= 1
            return True
        else:
            return False


    def use_destiny_point(self):
        if self.destiny_points > 0:
            self.destiny_points -= 1
            return True
        else:
            return False