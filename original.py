# Role playing game
# Original J.Timmins 2018
# Updated W.Carr 2023
#---------------------------Import modules--------------------------------------

from random import randint
# Used to generate random numbers

from time import sleep
# Used to implement a pause, or delay

#---------------------------Main game----------------------------------------

# Answer this in a comment - What do these next 3 instructions do?
#                            Change them to find out, but set them back to
#                            PAUSE = 1, turn = 0, your_score = 0
# Answer this in a comment - Why is PAUSE in capitals?
PAUSE = 1
turn = 0
your_score = 0

# Answer this in a comment - what does this next instruction do? What is it called?
while True:

    turn = turn + 1

    # Answer this in a comment - What does this block do?
    #                            Look at the word randint it's made of two words
    if your_score < 3:
        spawn = randint(0,2)
    elif your_score < 5:
        spawn = randint(0,3)
    else:
        spawn = randint(0,4)

    # Answer this in a comment - What does this block do?       
    teachers = ["Mr Smith", "Mr Cammack", "Mr Birchall", "Mr Soulsby", "Lord Timmins of Mobberley"]
    opponent = teachers[spawn]

    # Answer this in a comment - What does this block do?
    print("\n")
    print("o===[]:::::::::::::>\n")
    print("Turn: " + str(turn))
    print("Score: " + str(your_score))
    sleep(PAUSE)
    print("It is a dark time for students")
    sleep(PAUSE)
    print("You wander nervously through the hallowed halls of")
    print("Altrincham Grammar School for Boys")
    sleep(PAUSE)
    print("Dark creatures stalk the corridors")
    print()
    sleep(PAUSE)
    print("Out of the shadows steps...")
    sleep(PAUSE)
    print(opponent+"!")
    sleep(PAUSE)
    
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

    # Answer this in a comment - What does this instruction do?    
    choice = input("> ")

    # Answer this in a comment - What does this block do?
    if choice == "r":
        print("You run away, a wise choice")
    else:
        print("Be prepared to meet your doom...")
        sleep(PAUSE)
        # Answer this in a comment - What does this instruction do?
        your_attack = (randint(0,5)+1)
        # Answer this in a comment - What does this instruction do?
        opponent_attack = randint(0,2) + spawn

        # Fill in - What does this block do?
        if your_attack > opponent_attack:
            print("You fight...you win!")
            print(opponent + " is defeated!")
            your_score = your_score + (spawn+1)
        else:
            print("You fight...you lose!")
