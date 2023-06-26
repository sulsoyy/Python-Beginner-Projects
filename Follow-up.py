import random
#import time


# List of words that are inserted by a user
words = []

# List of initial_words

initial_words = ['Apple', 'Banana', 'Carrot', 'Durian', 'Eggplant', 'Figs', 'Grape', 'Hazelnuts', 
                'Icaco', 'Jalapeno', 'Kale', 'Lemon', 'Mango', 'Nectarine', 'Orange', 'Peanut', 
                'Quince', 'Raddish', 'Strawberry', 'Tomato', 'Ugli', 'Vanilla', 'Watermelon', 'Xoconostle', 'Yam', 'Zucchini']


integer = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Score

score = 0


# function

def check_word_ending():

    global score
    global n

    while score < n:

        word = words[len(words) - 1]
        last_letter = word[-1].capitalize()


        new_word = input("Type a word that starts with the last letter of " + word + " - " + last_letter + "\n").capitalize()
        check_word_integer(new_word)

        if new_word not in words:
            if new_word[0] == last_letter: 
                    new_word = new_word.capitalize()
                    words.append(new_word)
                    score += 1
                    print("Current Score: {}".format(str(score)))
        
        elif new_word in word or new_word[0] != last_letter:
            new_word = input("Type a word that starts with the last letter of " + word + " - " + last_letter + "\n").capitalize()



# Check if a word contain integer 


def check_word_integer(word):

    i = len(word)

    # check each index of string
    for l in range(i):
        if word[l] not in integer:
            continue 
        elif word[l] in integer:
            print("You can't type integer!")
            check_word_ending()
        


def scoring_system():
    pass
    



# Game Instruction

word = random.choice(initial_words)
words.append(word)



n = int(input("How many return do you want?"))

# Starting 
print("Score {} to win the game!".format(str(n)))
print("Current Score: {}".format(str(score)))



check_word_ending()


if score == n:
    print("Congratulation You Won the Game!")
    print(words)







'''
while score < 1:
    word = input("Type a word that starts with the last letter of " + initial_word + " - " + initial_word[-1].capitalize() + "\n").capitalize()

    check_word_integer(word)

    if word not in words:
            if word[0] == initial_word[-1].capitalize():
                word = word.capitalize()
                words.append(word)
                score += 1
                print("Current Score: {}".format(str(score)))

    else:
        word = input("Type a word that starts with the last letter of " + initial_word + " - " + initial_word[-1].capitalize() + "\n").capitalize()

print(words)

    
for score in range(1, 4):
    check_word_ending()


print("Congratulation You Won the Game!")
print(words)


# if input word includes integer 

'''