import random
#import time


# List of words that are inserted by a user
words = []

# List of initial_words

initial_words = ['Apple', 'Banana', 'Carrot', 'Durian', 'Eggplant', 'Figs', 'Grape', 'Hazelnuts', 
                'Icaco', 'Jalapeno', 'Kale', 'Lemon', 'Mango', 'Nectarine', 'Orange', 'Peanut', 
                'Quince', 'Raddish', 'Strawberry', 'Tomato', 'Ugli', 'Vanilla', 'Watermelon', 'Xoconostle', 'Yam', 'Zucchini']

# Score

score = 0


# function

def check_word_ending():
    
    word = words[len(words) - 1]
    last_letter = word[-1]

    new_word = input("Type a word that starts with the last letter of " + word + " - " + last_letter.capitalize() + "\n")

    if new_word not in words:
        if new_word[1] == last_letter: 
            new_word = new_word.capitalize()
            words.append(new_word)
            score += 1
            print("Current Score: {}".format(str(score)))
        
    else:
        new_word = input("Type a word that starts with the last letter of " + word + " - " + last_letter.capitalize() + "\n")



def scoring_system():
    pass
    



# Game Instruction

initial_word = random.choice(initial_words)
words.append(initial_word)


# Starting 
print("Score 15 to win the game!")
print("Current Score: {}".format(str(score)))


while score < 1:
    word = input("Type a word that starts with the last letter of " + initial_word + " - " + initial_word[-1].capitalize() + "\n")

    print(word[0] + initial_word[-1])

    if word not in words:
        if word[0] == initial_word[-1]:
            word = word.capitalize()
            words.append(word)
            score += 1
            print("Current Score: {}".format(str(score)))

    else:
        word = input("Type a word that starts with the last letter of " + initial_word + " - " + initial_word[-1].capitalize() + "\n")

print(words)

    
for score in range(2, 11):
    check_word_ending()


print("Congratulation You Won the Game!")
print(words)


# if input word is not captialised then it occurs errors
