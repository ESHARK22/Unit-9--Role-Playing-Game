from random import randint
from time import sleep

PAUSE = 1
turn = 0
your_score = 0

opponents = ["Mr Smith", "Mr Cammack", "Mr Birchall", "Mr Soulsby", "Lord Timmins of Mobberley"]
actions = ["run", "fight"]
items = ["sword", "shield", "potion"]

def display_intro():
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

def display_opponent(opponent):
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

def get_player_choice():
    choice = input("> ")
    return choice

def run_away():
    print("You run away, a wise choice")

def fight(opponent):
    global your_score
    print("Be prepared to meet your doom...")
    sleep(PAUSE)
    your_attack = randint(0, 5) + 1
    opponent_attack = randint(0, 2) + opponent

    if your_attack > opponent_attack:
        print("You fight...you win!")
        print(opponents[opponent] + " is defeated!")
        your_score += (opponent + 1)
    else:
        print("You fight...you lose!")

def bubble_sort(scores):
    n = len(scores)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if scores[j] < scores[j + 1]:
                scores[j], scores[j + 1] = scores[j + 1], scores[j]

# Additional lists
player_scores = []
player_items = []
player_actions = []

while True:
    turn += 1

    if your_score < 3:
        spawn = randint(0, 2)
    elif your_score < 5:
        spawn = randint(0, 3)
    else:
        spawn = randint(0, 4)

    opponent = opponents[spawn]

    display_intro()
    display_opponent(opponent)

    choice = get_player_choice()

    if choice == "r":
        run_away()
    else:
        fight(spawn)

    player_scores.append(your_score)
    player_items.append(items[randint(0, 2)])
    player_actions.append(actions[randint(0, 1)])

    bubble_sort(player_scores)

    print("\nPlayer Scores:")
    for score in player_scores:
        print(score)

    print("\nPlayer Items:")
    for item in player_items:
        print(item)

    print("\nPlayer Actions:")
    for action in player_actions:
        print(action)