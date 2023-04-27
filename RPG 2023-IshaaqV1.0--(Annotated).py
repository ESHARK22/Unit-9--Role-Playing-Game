# Role playing game
# Original J.Timmins 2018
# Updated W.Carr 2023
# Modified I.Ollite 2023
#---------------------------Import modules--------------------------------------

from random import randint
# Used to generate random numbers

from time import sleep
# Used to implement a pause, or delay

#---------------------------Main game----------------------------------------

# These next 3 instructions set the defualt variables and the starting variables 
PAUSE = 1 # -> This is the delay between each prompt. (It is in caps as it is a constant). (pauses add suspence)
turn = 0 # This var keeps track of which turn the player is on (How many times the player has gone round the game). 
your_score = 0 # This var keeps track of the players score. (starts off with zero points))

while True: # An iteratation that goes on until inturrupted

    turn = turn + 1
    
    # This selects an oppnent based on the users score. 
    # This makes the  game start off easy and progessivly gets hard.
    # When your score is under 3, you can get either get Mr Smith or Mr Cammack, or Mr Birchall
    # As you progress, You then get a higher change of being opposed by more powerfull opponents.
    if your_score < 3:
        spawn = randint(0,2)
    elif your_score < 5:
        spawn = randint(0,3)
    else:
        spawn = randint(0,4)

    # This block selects the opponents name depending on which "spawn" was generated.
    if spawn == 0:
        opponent = "Mr Smith"
    elif spawn == 1:
        opponent = "Mr Cammack"
    elif spawn == 2:
        opponent = "Mr Birchall"
    elif spawn == 3:
        opponent = "Mr Soulsby"
    else:
        opponent = "Lord Timmins of Mobberley"



    # This prints out somen narative and the user scores 
    print("\n") # 2 New lines
    print("o===[]:::::::::::::>\n") # Some ascii art
    print("Turn: " + str(turn)) # Print which turn the user is on
    print("Score: " + str(your_score)) # Print out the users score
    sleep(PAUSE) # delay for suspense 
    print("It is a dark time for students") # Some narative
    sleep(PAUSE) # delay for suspense 
    print("You wander nervously through the hallowed halls of") #Some narative
    print("Altrincham Grammar School for Boys") # Some narative
    sleep(PAUSE) # delay for suspense 
    print("Dark creatures stalk the corridors") # Some narative
    print() # New line
    sleep(PAUSE) # delay for suspense 
    print("Out of the shadows steps...") # Some narative
    sleep(PAUSE) # delay for suspense 
    print(opponent+"!") # Print out the players opponent
    sleep(PAUSE) # delay for suspense 
    
    # Ascii art
    print("")
    print(" _\|/^")
    print(" (_oo>")
    print("   |         O")
    print("  /|\\       /|\\")
    print("   |         |")       
    print("   LL        LL")
    print("\n")
    print(opponent + " towers over you. Do you fight, or do you run?")
    print("Enter f or r")
    
    # The instruction "choice = input("> ")" prompts the player to enter a choice (f for fight, r for run) 
    # and assigns the input to the variable choice.
    choice = input("> ")

    # The block starting with "if choice == 'r':" checks if the player chose to run and prints a message accordingly. 
    # If the player chose to fight, the block starting with "else:" generates two random numbers (one for the player's 
    # attack and one for the opponent's attack), compares them, and prints a message indicating whether 
    # the player won or lost. If the player won, their score is increased based on the value of spawn.

    if choice == "r": 
        # Checking if the player chose to run and printing a message accordingly.
        print("You run away, a wise choice")
    else:
        # If the player chose to fight, generating two random numbers for the player's attack and 
        # the opponent's attack, comparing them, and printing a message indicating whether the player won or lost.

        print("Be prepared to meet your doom...")
        sleep(PAUSE) # delay for suspense 
        # This generates a random number for the users attack 
        your_attack = (randint(0,5)+1)
        # This generates a random number for the users attack
        opponent_attack = randint(0,2) + spawn # This generates a random number for the opponents attack
        
        # opponent_attack = 0  :) [A little cheat] 
        
        if your_attack > opponent_attack: # This checks if the users attack is greater than the opponents attack
            print("You fight...you win!") # This tells the user they have won
            print(opponent + " is defeated!") 
            your_score = your_score + (spawn+1) # This increases the users score depending on the spawn.
        else:
            print("You fight...you lose!")
