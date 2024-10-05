import json
from pathlib import Path
import random
import sys

alphabet = [chr(i) for i in range(97,123)]
vowels = ["a","e","i","o","u"]
only_consonants = []
for l in alphabet:
    if l not in vowels:
        only_consonants.append(l)

print(only_consonants)

def word_generator():
    length = random.randint(3,15)
    new_word = []
    next_consonant = False
    next_vowel = False

    for x in range(0,length):
        if next_consonant:
            n_w_l = only_consonants[random.randint(0,20)]
            next_consonant = False
        elif next_vowel:
            n_w_l = vowels[random.randint(0,4)]
        else:
            n_w_l = alphabet[random.randint(0,25)]

        if x>=1:
            if n_w_l in vowels and new_word[x-1] in vowels:
                next_consonant = True
            elif n_w_l in only_consonants and new_word[x-1] in only_consonants:
                next_vowel = False
        
        new_word.append(n_w_l)
    new_word_str = "".join(new_word)
    
    return new_word_str

def new_dictionary(word,word_def):
    cool_words[word] = word_def
    return cool_words

def save_dict(words):
    word_file = Path("new_words.json")
    words_for_file = json.dumps(words)
    word_file.write_text(words_for_file)

if __name__ == "__main__":
    try:
        cool_words = json.loads("new_words.json")
    except:
        cool_words = {"myaur":"The sound that a battle cat makes."}

    done = False
    while not done:
        prompt = input("Would you like to make a random word? (Type 'No' to exit.) ")
        if prompt == "No":
            done = True
        else:
            result = word_generator()
            if cool_words != None and result in cool_words.keys():
                want_def = input(f"{result} is already a word! Want to hear its definition? (Type 'No' to go back.) ")
                if want_def != "No" and want_def != "no":
                    print(f"{result}: {cool_words[result]}")
            else:
                print(f"Your new word is {result}.")
                want_def = input("Would you like to give the word a meaning? (Type 'No' to go back.) ")
                if want_def != "No":
                    new_def = input("Please give the word a short description, like you'd see in a dictionary.")
                    new_dictionary(result,new_def)
                    print("Here's your current dictionary!")
                    for k,v in cool_words.items():
                        print(k + " : " + v)
    if cool_words != {}:
        save_dict(cool_words)
    sys.exit()