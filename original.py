# Role playing game
# Original J.Timmins 2018
# Updated W.Carr 2023
# Modified by J Yanni 2023
#---------------------------Import modules--------------------------------------

def bubble_sort(unsorted_list):
    n = len(unsorted_list)

    # Traverse through all array elements
    for i in range(n - 1):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Swap if the element found is greater than the next element
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list



from random import randint
# Used to generate random numbers

 

from time import sleep
# Used to implement a pause, or delay

user_name = input("What is your name? ")

    

#---------------------------Main game----------------------------------------

# Print a leaderboard
print("Leaderboard:")
users = []
users_scores = []
leaderboard = []


with open("scores.txt", "r") as scores_file:
    scores = scores_file.readlines()
    for score in scores:
        user = score.split(":")[0]
        score = score.split(":")[1]
        score = score.replace("\n", "")
        leaderboard.append([user, score])   
# Bubble sort the leaderboard
leaderboard = bubble_sort(leaderboard)[::-1]

leaderboard_str = ""
for i in range(len(leaderboard)):
    leaderboard_str += str(i+1) + leaderboard[i][0] + ": " + leaderboard[i][1] + "\n"
print(leaderboard_str)
 

# Answer this in a comment - What do these next 3 instructions do? 
#                            Change them to find out, but set them back to#                            PAUSE = 1, turn = 0, your_score = 0
# Answer this in a comment - Why is PAUSE in capitals? PAUSE does not change and is a constant
PAUSE = 1 #  Puts a delay in your program and tries to build up suspense
turn = 0 #how many times you have played the game
your_score = 0 #Shows you your score and changes it

lives = 2
player_health = 80

characters = [
    "john",
    "ogo",
    "eli"
]
character_health = [
    100,
    80,
    60
]
print("Choose your character:")
for i in range(len(characters)):
    print(" -> " + characters[i])

user_character = input("->").lower()
if user_character in characters:
    print("You chose", user_character)
    player_health = character_health[characters.index(user_character)] # Index gets the position of the item in the list
else:
    print("That character doesn't exist!")
    exit()


# Answer this in a comment - what does this next instruction do? What is it called? This is an iteration
while True:
 

    turn = turn + 1

 

    # Answer this in a comment - What does this block do? Selection
                                 #Selects a random number
    #                            Look at the word randint it's made of two words

    if your_score < 3:# based on your score and chooses your spawn based on your score
        spawn = randint(0,2)
    elif your_score < 5:
        spawn = randint(0,3)
    else:
        spawn = randint(0,5)

    

        # Answer this in a comment - What does this block do? This gives variables to teachers and gives them a number to help give it a spawn from before      

    

    teachers=["Mr Smith","Mr Cammack","Mr Birchall","Lord Timmins of Mobberley", "Dr Marsden"]
    teacher_health=[60,70,80,90,100]
    opponent=teachers[spawn]

    

    background=["The Dark Corridors of History","The Depths of the Maths Block","The Spooky Rooms of Technology"
                    ,"The Abyss of The Sounth Yard","The Cold Music Rooms","The Blanket of Fog"
                    ,"The Vastness of The Physics Block"]
    room=background[spawn]

    


    

    items=["Sword","Mace","Katana","Pencil","Nunchucks","Brass Knuckles"]
    item_strength=[10,20,30,40,50,60]
    items = bubble_sort(items)
    


    def Smith():
        print("")
        print(" ___")
        print("(_oo>")
        print("   |         O")
        print("  /|\\       /|\\")
        print("   |         |")       
        print("   LL        LL")

    

    def Cammack():
        print("")
        print(" ////")
        print("(_oo>")
        print(" (|)         O")
        print(" /|\\       /|\\")
        print("  |         |")       
        print("  LL        LL")

    

    def Birchall():
        print("")
        print(" ^^^^")
        print("(_oo>")
        print(" (|)         O")
        print(" /|\\       /|\\")
        print("   |         |")       
        print("   LL        LL")

    

    def Lord():
        print("")
        print(" ^^^^")
        print("(_oo>")
        print(" (|)         O")
        print(" /|\\       /|\\")
        print("   |         |")       
        print("   LL        LL")

    

        # Answer this in a comment - What does this block do? This is the narrative
    print("\n")
    print("o===[]:::::::::::::>\n") #ASCII art
    print("Turn: " + str(turn)) #Adds in the number for your turn
    print("Score: " + str(your_score)) #Adds in the number for your score
    print("Lives: " + str(lives)) #Adds in the number for your lives
    sleep(PAUSE)
    print("It is a dark time for students")
    sleep(PAUSE)
    print("You wander nervously through the hallowed halls of")
    print("Altrincham Grammar School for Boys")
    sleep(PAUSE)
    print("Dark creatures stalk the corridors")
    print()
    sleep(PAUSE)
    print("Out of")
    print(room, "steps...")
    sleep(PAUSE)
    print(opponent+"!")
    sleep(PAUSE)

    

    if opponent=="Mr Smith":
        Smith()
    if opponent=="Mr Cammack":
        Cammack()
    if opponent=="Mr Birchall":
        Birchall()
    if opponent=="Lord Timmins of Mobberley":
        Lord()

    print("\n")
    print(opponent + " towers over you. Do you fight, or do you run?")
    print("Enter f or r")

    

        # Answer this in a comment - What does this instruction do?    
    choice = input("> ")

    

        # Answer this in a comment - What does this block do?
    if choice == "r":
        print("You run away, a wise choice")
    else:
        print(", ".join(items))
        weapoons=input("Choose your weapon:")
        print("Be prepared to meet your doom...")
        sleep(PAUSE)
            # Answer this in a comment - What does this instruction do?
            # Index gets the position of the item in the list
        your_attack = (randint(5,45)) + item_strength[items.index(weapoons)] 
            # Answer this in a comment - What does this instruction do?
        opponent_attack = randint(5,45) + teacher_health[teachers.index(opponent)]

    # Your attack should take away from the opponent's health
    # The opponent's attack should take away from your health
    # If either of you have health <= 0, you die

    teacher_health = teacher_health[teachers.index(opponent)] - your_attack
    player_health = player_health - opponent_attack

    print("You attacked", opponent, "with", weapoons, "for", your_attack, "damage")
    print(opponent, "attacked you for", opponent_attack, "damage")

    print("Your health:", player_health)
    print(opponent, "health:", teacher_health)

    if teacher_health <= 0:
        print("You killed", opponent)
        your_score = your_score + 1
        print("Your score is now", your_score)

    if player_health <= 0:
        print("You died")
        lives = lives - 1
        print("You have", lives, "lives left")
    if not teacher_health <= 0 and not player_health <= 0:
        print("You both survived")




    if lives == 0:
        print("You have no lives left")
        print("Game Over")
        break



# Save the users score to a file
# "a" means append
with open("scores.txt", "a") as scores_file:
    scores_file.write(user_name + ": " + str(your_score) + "\n")