from mechanics import *
from heroic_character import *
from tkinter import *
from PIL import ImageTk,Image
import pickle 

def character_sheet(character):
	chara = Tk()
	chara.geometry('450x600')

	image = Image.open("images/font.png")
	background_image = ImageTk.PhotoImage(image)

	background_label = Label(chara, image=background_image)
	background_label.image = background_image
	background_label.place(x=0, y=0, relwidth=1, relheight=1)

	# Basic Info
	name_lable = Label(chara, text='Name: ' + character.name)
	player_label = Label(chara, text='PLAYER PLACE HOLDER')
	class_label = Label(chara, text='CLASS PLACE HOLDER')
	species_label = Label(chara, text='Species: ' + character.species)
	level_lable = Label(chara, text='Level: ' + str(character.level))

	
	# Abilities
	score_label = Label(chara, text='Score')
	mod_label = Label(chara, text='Mod')

	str_label = Label(chara, text='Strength:')
	str_value_label = Label(chara, text=str(character.stre))
	str_mod_label = Label(chara, text=str(character.stre_mod()))

	dex_label = Label(chara, text='Dexterity:')
	dex_value_label = Label(chara, text=str(character.dex))
	dex_mod_label = Label(chara, text=str(character.dex_mod()))

	con_label = Label(chara, text='Constitution:')
	con_value_label = Label(chara, text=str(character.con))
	con_mod_label = Label(chara, text=str(character.con_mod()))

	int_label = Label(chara, text='Intelligence:')
	int_value_label = Label(chara, text=str(character.inte))
	int_mod_label = Label(chara, text=str(character.inte_mod()))

	wis_label = Label(chara, text='Wisdom:')
	wis_value_label = Label(chara, text=str(character.wis))
	wis_mod_label = Label(chara, text=str(character.wis_mod()))

	cha_label = Label(chara, text='Charisma:')
	cha_value_label = Label(chara, text=str(character.cha))
	cha_mod_label = Label(chara, text=str(character.cha_mod()))



# Grids
	name_lable.grid(	column = 0, row = 0)
	player_label.grid(	column = 1, row = 0)
	class_label.grid(	column = 0, row = 1)
	species_label.grid(	column = 1, row = 1)
	level_lable.grid(	column = 2, row = 1)

	score_label.grid(	column = 1, row = 2)
	mod_label.grid(		column = 2, row = 2)

	str_label.grid(column = 0, row = 3)
	dex_label.grid(column = 0, row = 4)
	con_label.grid(column = 0, row = 5)
	int_label.grid(column = 0, row = 6)
	wis_label.grid(column = 0, row = 7)
	cha_label.grid(column = 0, row = 8)
	str_value_label.grid(column = 1, row = 3)
	dex_value_label.grid(column = 1, row = 4)
	con_value_label.grid(column = 1, row = 5)
	int_value_label.grid(column = 1, row = 6)
	wis_value_label.grid(column = 1, row = 7)
	cha_value_label.grid(column = 1, row = 8)
	str_mod_label.grid(column = 3, row = 3)
	dex_mod_label.grid(column = 3, row = 4)
	con_mod_label.grid(column = 3, row = 5)
	int_mod_label.grid(column = 3, row = 6)
	wis_mod_label.grid(column = 3, row = 7)
	cha_mod_label.grid(column = 3, row = 8)

	chara.mainloop()


def auto_create():
	pass

def manual_create():
	char_input()

def character_management(character):
	save_name = character.name + str(character.level)
	# Used to save character
	def save_character():
	    # Its important to use binary mode 
	    file = open(save_name, 'ab')

	    # source, destination 
	    pickle.dump(character, file)                      
	    file.close() 

	def show_character_sheet():
		character_sheet(character)
	
	char_page = Tk()

	name_lable = Label(char_page, text='Name: ' + character.name)
	name_lable.grid(column = 0, row = 0)

	level_lable = Label(char_page, text='Level ' + str(character.level))
	level_lable.grid(column = 1, row = 0)

	level_button = Button(char_page, text='Level Up')
	level_button.grid(column = 0, row = 1)


	sheet_button = Button(char_page, text='Character Sheet',\
	  	command=show_character_sheet)
	sheet_button.grid(column = 1, row = 1)


	save_button = Button(char_page, text='Save Character', \
        command=save_character)
	save_button.grid(column = 2, row = 1)



def load_menu():
	def load_character():
		load_name = str(location_input.get())
		file = open(load_name, 'rb')
		chara = pickle.load(file)
		file.close()
		load_menu.destroy()
		character_management(chara)


	load_menu = Tk()

	location = Label(load_menu, text="Save location")
	location.grid(column = 0, row = 0)

	location_input = Entry(load_menu)
	location_input.grid(column = 1, row = 0)

	load_button = Button(load_menu, text='Load', command=load_character)
	load_button.grid(column = 1, row = 1)

def char_input():
	def get_values():
		abilities = list()
		abilities.append(int(str_input.get()))
		abilities.append(int(dex_input.get()))
		abilities.append(int(con_input.get()))
		abilities.append(int(int_input.get()))
		abilities.append(int(wis_input.get()))
		abilities.append(int(cha_input.get()))
		# confirm input ########### confirm input ########### confirm input ########### confirm input ########### confirm input ########### confirm input ##########

		name = name_input.get()
		owner = owner_input.get()
		species = selected_species.get()
		char_class = selected_class.get()

		new_character = HeroicCharacter(name, owner, species, abilities)
		new_character.level_up(char_class)
		
		character_management(new_character)
		char_form.destroy()


	char_form = Tk()
	char_form.geometry('400x450')

	# Name
	name_text = Label(char_form, text="Character Name: ")
	name_text.grid(column = 0, row = 1)
	name_input = Entry(char_form)
	name_input.grid(column = 1, row = 1)

	owner_text = Label(char_form, text="Creater/Owner's Name: ")
	owner_text.grid(column = 0, row = 2)
	owner_input = Entry(char_form)
	owner_input.grid(column = 1, row = 2)

	# Species
	selected_species = StringVar(char_form)
	selected_species.set('Bothan')
	species_list = ['Human', 'Bothan', 'Cerean', 'Duros', 'Ewok', 'Gamorrean',\
				  'Gungan', 'Ithorian', 'Kel Dor', 'Mon Calamari', 'Quarren', \
				  'Rodian', 'Sullustan', 'Trandoshan', 'Twilek', 'Wookiee', \
				  'Zabrak']
	species_list.sort()
	species_text = Label(char_form, text="Species: ")
	species_text.grid(column = 0, row = 3) 
	species_input = OptionMenu(char_form, selected_species, *species_list)
	species_input.grid(column = 1, row = 3)

	# Class
	selected_class = StringVar(char_form)
	selected_class.set('Jedi')
	class_list = ['Jedi', 'Scout', 'Soldier', 'Scoundrel', 'Noble']
	class_list.sort()
	class_text = Label(char_form, text="Initial Class: ")
	class_text.grid(column = 0, row = 4) 
	class_input = OptionMenu(char_form, selected_class, *class_list)
	class_input.grid(column = 1, row = 4)

	# STR
	str_text = Label(char_form, text="Strength: ")
	str_text.grid(column = 0, row = 5)
	str_input = Entry(char_form)
	str_input.grid(column = 1, row = 5)

	# DEX
	dex_text = Label(char_form, text="Dexterity: ")
	dex_text.grid(column = 0, row = 6)
	dex_input = Entry(char_form)
	dex_input.grid(column = 1, row = 6)

	# CON
	con_text = Label(char_form, text="Constitution: ")
	con_text.grid(column = 0, row = 7)
	con_input = Entry(char_form)
	con_input.grid(column = 1, row = 7)

	# INT
	int_text = Label(char_form, text="Intelligence: ")
	int_text.grid(column = 0, row = 8)
	int_input = Entry(char_form)
	int_input.grid(column = 1, row = 8)

	# WIS
	wis_text = Label(char_form, text="Wisdom: ")
	wis_text.grid(column = 0, row = 9)
	wis_input = Entry(char_form)
	wis_input.grid(column = 1, row = 9)

	# CHA
	cha_text = Label(char_form, text="Charisma: ")
	cha_text.grid(column = 0, row = 10)
	cha_input = Entry(char_form)
	cha_input.grid(column = 1, row = 10)

	# Button
	submit_button = Button(char_form, text="Submit", command=get_values)
	submit_button.grid(column = 2, row = 11)

	char_form.mainloop()


# Used to get abilities to increament on specific levels
def get_abilities(name):
	abil_form = Tk()
	abil_form.geometry('300x300')

	abil_form_label = Label(abil_form, text="Select two abilities to increase \
		by one.")
	abil_form_label.pack()
	abil = Checkbar(abil_form, ['Strength', 'Dexterity', 'Constitution', \
		'Intelligence', 'Wisdom', 'Charisma'])
	abil.pack()

	return [0,0,0,0,1,1]


def main_menu():
	main = Tk()
	main.geometry('300x300')

	load = Button(main, text="Load Character", command=load_menu)
	load.pack()

	autoCreate = Button(main, text="Auto-Create Character", command=auto_create)
	autoCreate.pack()

	manualCreate = Button(main, text="Manually Create Character", \
		command=manual_create)
	manualCreate.pack()

	main.mainloop()

main_menu()