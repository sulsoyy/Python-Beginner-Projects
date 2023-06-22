import random


# List of words that are inserted by a user

words = []


# List of initial_words

initial_words = ['Apple', 'Banana', 'Carrot', 'Durian', 'Eggplant', 'Figs', 'Grape', 'Hazelnuts', 'Icaco', 'Jalapeno', 'Kale', 'Lemon', 'Mango', 'Nectarine', 'Orange', 'Peanut', 'Quince', 'Raddish', 'Strawberry', 'Tomato', 'Ugli', 'Vanilla', 'Watermelon', 'Xoconostle', 'Yam', 'Zucchini']

# Score

score = 0


# function

def check_word_ending():
    if word not in words:
            word = input("Type a word that starts with " + word[-1].capitalize() + "\n").capitalize()
            words.append(word)
            score += 1

    else:
        word = input("Type a word that starts with " + word[-1].capitalize() + "\n").capitalize()




# Game Instruction

initial_word = random.choice(initial_words)
words.append(initial_word)

word = input("Type a word that starts with the last letter of " + initial_word + " - " + initial_word[-1].capitalize() + "\n").capitalize()

while score <= score + 1:
    if word not in words:
            word = input("Type a word that starts with " + word[-1] + "\n")
            words.append(word)
            score += 1

    elif word in words:
        word = input("Type a word that starts with the last letter of " + initial_word + " - " + initial_word[-1].capitalize() + "\n").capitalize()

    break








