import random

PLAYER_IS_ALIVE = True
PLAYER_WON = False
NUM_DIGITS = 3
NUM_GUESSES = 10
pico = False
fermi = False
bagels = False

def main():
    global PLAYER_IS_ALIVE, PLAYER_WON
    print("""Bagels, a deductive logic game. \n
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:\n
When I say: That means: \n
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.
 Bagels No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.""")
    
    #main game loop
    while PLAYER_IS_ALIVE :
        print("do you want to play ?")
        if input("> ").lower().startswith('y'):
            game_loop()
        else:
            PLAYER_IS_ALIVE = False


    
def game_loop():
        secretNumber = getSecretNumber()
        guess_loop(secretNumber)
        if PLAYER_WON:
            print("good game ! you got it")
        else:
            print("you ran out of guesses, the answer was " + secretNumber)
    


def getSecretNumber():
    secretDigit = ''
    for i in range(NUM_DIGITS):
        secretDigit += str(random.randint(0,9))

    return secretDigit    

def guess_loop(secretDigit):
    i = 1
    while i < 11 and not PLAYER_WON:
        print("GUESS #{}".format(i))
        playerDigit = input("> ")
        if len(playerDigit) > 0 and len(playerDigit) < 4:
            i = i + 1
            check_loop(playerDigit, secretDigit)
            displayResult()
        else:
            print("Give a 3 digit number")          

def check_loop(playerDigit, secretDigit):
    global pico, fermi, bagels, PLAYER_WON
    pico = False
    fermi = False
    bagels = False
    PLAYER_WON = False

    if playerDigit == secretDigit:
        PLAYER_WON = True
    else :    
        i = 0
        while not pico and not fermi and i < NUM_DIGITS:
            if playerDigit[i] == secretDigit[i]:
                fermi = True
            else:
                for j in range(1,NUM_DIGITS):    
                    if secretDigit[i] == playerDigit[j]:
                        pico = True

            i = i + 1             

        if not fermi and not pico:
            bagels = True                

def displayResult():
    if fermi:
        print("fermi")
    elif pico:
        print("pico")
    elif bagels:
        print("bagels")    

main()