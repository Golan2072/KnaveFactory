#knavefac.py
#Knave tabletop RPG character generator
#v0.1, July 11th, 2022
#By Omer Golan-Joel

import stellagama
import random

def name_gen (sex):
    if sex == "female":
        return stellagama.random_line("femalenames.txt")
    elif sex == "male":
        return stellagama.random_line("malenames.txt")

def ability_gen():
    return min(stellagama.dice(1,6), stellagama.dice(1,6), stellagama.dice(1,6))

def equipment_gen(background):
    equipment = []
    equipment.append ("2 rations")
    equipment.append (random.choice(["dagger", "cudgel", "sickle", "staff", "spear", "sword", "mace", "axe", "flail", "halberd", "warhammer", "long sword", "battle axe", "sling and 20 bullets", "bow and 20 arrows", "crossbow and 20 bolts"]))
    armor_roll = stellagama.dice(1, 20)
    if armor_roll in range (1, 3):
        pass
    if armor_roll in range (4, 14):
        equipment.append ("gambeson")
    if armor_roll in range (15, 19):
        equipment.append ("brigandine")
    if armor_roll == 20: equipment.append ("chain")
    helmet_roll = stellagama.dice(1, 20)
    if helmet_roll in range (1, 13):
        pass
    if helmet_roll in range (14, 16):
        equipment.append ("helmet")
    if helmet_roll in range (17, 19):
        equipment.append ("shield")
    if helmet_roll == 20:
        equipment.append ("shield")
        equipment.append ("helmet")
    for i in range (0,2):
        equipment.append(random.choice(["rope, 50m", "pulleys", "5 candles", "chain, 10ft", "10 chalk", "crowbar", "tinderbox", "grappling hook", "hammer", "waterskin", "lantern", "lamp oil", "padlock", "manacles", "mirror", "pole, 10 ft", "sack", "tent", "5 spikes", "5 torches"]))
    equipment.append(random.choice(["air bladder", "bear trap", "shovel", "bellows", "grease", "saw", "bucket", "drill", "fishing rod", "marbles", "glue", "pick", "hourglass", "net", "tongs", "lockpicks", "metal file", "nails"]))
    equipment.append(random.choice(["incense", "sponge", "lens", "perfume", "horn", "bottle", "soap", "spyglass", "tar pot", "twine", "fake jewels", "blank book", "card deck", "dice set", "cook pots", "face paint", "whistle", "instrument", "quill and ink", "small bell"]))
    return equipment

class Knave():
    def __init__(self):
        self.sex = random.choice(["female", "male"])
        self.name = name_gen(self.sex)
        self.background = "knave"
        self.level = 1
        self.strength = ability_gen()
        self.strength_defense = self.strength + 10
        self.dexterity = ability_gen()
        self.dexterity_defense = self.dexterity + 10
        self.constitution = ability_gen()
        self.constitution_defense = self.constitution + 10
        self.intelligence = ability_gen()
        self.intelligence_defense = self.intelligence + 10
        self.wisdom = ability_gen()
        self.wisdom_defense = self.wisdom + 10
        self.charisma = ability_gen()
        self.charisma_defense = self.charisma + 10
        self.copper = 0
        self.hp = stellagama.dice (1, 8)
        self.equipment = equipment_gen(self.background)
        self.physique = random.choice(["athletic", "brawny", "corpulent", "delicate", "gaunt", "hulking", "lanky", "ripped", "rugged", "scrawny", "short", "sinewy","slender", "flabby", "statuesque", "stout", "tiny", "towering", "willowy", "wiry"])
        self.face = random.choice(["bloated", "blunt", "bony", "chiseled", "delicate", "elongated", "patrician", "pinched", "hawkish", "broken", "impish", "narrow", "ratlike", "round", "sunken", "sharp", "soft", "square", "wide", "wolfish"])

knave = Knave()
print (f"{knave.name}, {knave.sex} human, level {knave.level}, STR +{knave.strength}, DEX +{knave.dexterity}, CON +{knave.constitution}, INT +{knave.intelligence}, WIS +{knave.wisdom}, CHA +{knave.charisma}, {knave.hp} HP")
print (f"Equipment: {', '.join(knave.equipment)}")
print(f"Physique: {knave.physique}, Face: {knave.face}")
