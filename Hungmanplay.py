from words import words
import random
import string
from deign_of_hangman import design

def get_a_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.upper()
def hungman():
    valid_word = get_a_valid_word(words)
    valid_word_letter = set(valid_word)
    alphabetic_series = set(string.ascii_uppercase)
    used_letter = set()
    lives = 5
    ## inputs
    while len(valid_word_letter)>0 and lives >0:
        print(f"you have {lives} lives, used letters: {''.join(used_letter)}")
        design(lives)
        word_list = [letter if letter in used_letter else "-" for letter in valid_word]
        print("Current words are:",''.join(word_list))
        user_letter = input("guess the word!: ").upper()
        if user_letter in alphabetic_series and user_letter not in used_letter:
            used_letter.add(user_letter)
            # print(user_letter)
            if user_letter in valid_word_letter:
                valid_word_letter.remove(user_letter)
                # print(valid_word_letter)
            else:
                lives = lives-1
                print("letter is not in word")
        elif user_letter in used_letter:
            print(f"This character already used. Please select Diffrent letter!!")
        else:
            print("INVALID LETTER!!!!!!!!!")
    if lives==0:
        design(0)
        print("Game Over!!  MAN is HANGED and the letter was",valid_word)
    else:
        print("yay!, You saved the man and the words was,",valid_word)
hungman()