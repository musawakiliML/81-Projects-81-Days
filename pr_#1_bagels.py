'''Bagels,

A deductive logic game, you  must guess a secret three-digit number  based on clues. The game offers one of  the following hints in response to your guess:  “Pico” when your guess has a correct digit in the  wrong place, “Fermi” when your guess has a correct  digit in the correct place, and “Bagels” if your guess  has no correct digits. You have 10 tries to guess the secret number.

Day #1 Project - Bagels

@ Created By Musa Adamu Wakili
    Blog:musawakiliml.hashnode.
    Repo:musawakiliML
'''

import random # importing the random libary for random selection of secret number

num_digits = 4 # setting the number of digits to guess
max_guesses = 10 # setting the number of trials you have

# main function of the game
def main():
    print("")
    
    while True:
        secret_num = get_secret_num()
        
        num_guesses = 1
        
        while num_guesses <= max_guesses:
            guess = ""
            
            while len(guess) != num_digits or not guess.isdecimal():
                guess = input('> ')
            
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1
            
            if guess == secret_num:
                break
            if num_guesses > max_guesses:
                print("out of guesses")
            

def get_secret_num():
    numbers = list("0123456789")
    random.shuffle(numbers)
    
    secret_num = ''
    
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num

def get_clues(guess, secret_num):
    
    if guess == secret_num:
        return "You Got It"
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
    return "".join(clues)


if __name__ == "__main__":
    main()
