import json
from pathlib import Path
import random

#fighter_file = Path("word_fighters.json")
#try:
#    contents = fighter_file.read_text()
#    a_t_f = json.loads(contents)
#except:
#    a_t_f = {}


# you can't make the Fighter class into a JSON object :(

a_t_f = {}

class Fighter:
    def __init__(self,word):
        self.part = part_speech(word)
        self.length = len(word)
        self.power = len(word)-vowel_count(word)
        self.name = word
        self.battle_hp = len(word)

        
    def attack(self,target):
        hit = self.power*random.randint(0,2)
        if hit == 0:
            print(f"{self.name}'s attack missed!")
        else:
            print(f"{target.name} just took a hit with {hit} power!")
            target.battle_hp -= hit

    def recover(self):
        self.battle_hp = len(self.name)


def vowel_count(word):
    count = 0
    for x in word:
        if x in ["a","e","i","o","u"]:
            count += 1
    return count

def part_speech(word):
    options = {"1":"Noun",
               "2":"Adjective",
               "3":"Verb"}
    selected = False
    while not selected:
        p_s = input(f"What part of speech is this fighter?\n1: Noun\n2: Adjective\n3: Verb\n")
        if p_s not in options.keys():
            print("That isn't an available option. Please try again.\n")
        else:
            print(f"Now this {options[p_s]} is ready to fight!")
            return options[p_s]

def fighter_add(word):
    a_t_f[word] = Fighter(word)
    return a_t_f

def fight_prep(cool_words):
    print("It's time to get your words ready for battle!")
    print("In case you need a refresher, your current fighting words are:")
    for k,v in cool_words.items():
        print(k + " : " + v)
    done = False
    while not done:
        new_fighter = input("Which word do you want to make a fighter? ")
        if new_fighter not in cool_words.keys():
            print("I couldn't find that word in your dictionary. Please try again.")
        else:
            fighter_add(new_fighter)
            more_fighters = input("Make another fighter? (Enter 'No' to go back.) ")
            if more_fighters == "No":
                done = True
            else:
                print("Let's continue, then.")

def word_fight(cool_words):
    print("First, choose which words will fight!")

    ready1 = False
    ready2 = False
    while not ready1:
        fighter_1 = input("The first fighter will be: ")
        if fighter_1 not in a_t_f.keys():
            print("That word doesn't seem to be a fighter. Please try again.")
        else:
            fighter_1 = a_t_f[fighter_1]
            type1 = fighter_1.part
            print(f"{fighter_1.name} the {type1} is ready to go!")
            ready1 = True
    
    while not ready2:
        fighter_2 = input("The second fighter will be: ")
        if fighter_2 not in a_t_f.keys():
            print("That word doesn't seem to be a fighter. Please try again.")
        else:
            fighter_2 = a_t_f[fighter_2]
            type2 = fighter_2.part
            print(f"{fighter_2.name} the {type2} is ready to go!")
            ready2 = True

    if fighter_1.length > fighter_2.length:
        print(f"Looks like {fighter_1.name} is up first!")
        go_first = 2
    elif fighter_1.length <= fighter_2.length:
        print(f"Looks like {fighter_2.name} is up first!")
        go_first = 1

    while fighter_1.battle_hp != 0 and fighter_2.battle_hp != 0:
        if go_first == 1:
            fighter_1.attack(fighter_2)
            fighter_2.attack(fighter_1)
        elif go_first == 2:
            fighter_2.attack(fighter_1)
            fighter_1.attack(fighter_2)
    if fighter_1.battle_hp == 0:
        print(f"It looks like {fighter_2.name} the {fighter_2.part} is victorious!")
        print(f"Maybe this means {cool_words[fighter_2.name]} is superior to {cool_words[fighter_1.name]}?")
    if fighter_2.battle_hp == 0:
        print(f"It looks like {fighter_2.name} the {fighter_2.part} is victorious!")
        print(f"Maybe this means {cool_words[fighter_2.name]} is superior to {cool_words[fighter_1.name]}?")

    print("No words were harmed in the making of this battle!")
    fighter_1.recover()
    fighter_2.recover()
    
    #fighter_file = Path("word_fighters.json")
    #fighter_list = json.dumps(a_t_f)
    #fighter_file.write_text(fighter_list)