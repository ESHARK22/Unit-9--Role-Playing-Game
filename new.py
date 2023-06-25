import json
from random import randint
from random import choice as random_choice
from time import sleep

#region fancy_print and fancy_input functions and Colors class

class Colours:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"

    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

def fancy_print(text: str, colour: Colours = Colours.RESET, bold: bool = False, underline: bool = False, wait_time: int = 0) -> None:
    """ 
    Prints text in a fancy way

    Parameters:
        text (str): text to be printed
        colour (Colours): colour of the text
        bold (bool): whether the text should be bold
        underline (bool): whether the text should be underlined

    Returns:
        None
    """

    print(colour + (Colours.BOLD if bold else "") + (Colours.UNDERLINE if underline else "") + text + Colours.RESET)
    sleep(wait_time)

def fancy_input(text: str, colour: Colours = Colours.RESET, bold: bool = False, underline: bool = False, wait_time: int = 0) -> str:
    """ 
    Gets input from the user in a fancy way

    Parameters:
        text (str): text to be printed
        colour (Colours): colour of the text
        bold (bool): whether the text should be bold
        underline (bool): whether the text should be underlined

    Returns:
        str: user input
    """

    return input(colour + (Colours.BOLD if bold else "") + (Colours.UNDERLINE if underline else "") + text + Colours.RESET)


def print_logo():
    fancy_print("Welcome to...", Colours.RED, bold=True, wait_time=1)
    logo = """


  ______     _                _    ___  ___  _       _____  _____   _____                              
 |  ____|   | |              | |  |__ \|__ \( )     |  __ \|  __ \ / ____|                             \n | |__   ___| |__   __ _ _ __| | __  ) |  ) |/ ___  | |__) | |__) | |  __    __ _  __ _ _ __ ___   ___ \n |  __| / __| '_ \ / _` | '__| |/ / / /  / /  / __| |  _  /|  ___/| | |_ |  / _` |/ _` | '_ ` _ \ / _ \\\n | |____\__ | | | | (_| | |  |   < / /_ / /_  \__ \ | | \ \| |    | |__| | | (_| | (_| | | | | | |  __/\n |______|___|_| |_|\__,_|_|  |_|\_|____|____| |___/ |_|  \_|_|     \_____|  \__, |\__,_|_| |_| |_|\___|\n                                                                             __/ |\n                                                                            |___/                      
    """

    fancy_print(logo, Colours.PURPLE, True, wait_time=1)
print_logo()
#endregion fancy_print and fancy_input functions and Colors class

#region Leaderboard - Initialisation
# Load the leaderboard from leaderboard.json and store it in a variable
try:
    with open("leaderboard.json", "r", encoding="UTF-8") as leaderboard_file:
        leaderboard = json.load(leaderboard_file)
except FileNotFoundError:
    # Make a new leaderboard if leaderboard.json does not exist
    leaderboard = {}
    with open("leaderboard.json", "w", encoding="UTF-8") as leaderboard_file:
        leaderboard_file.write(json.dumps(leaderboard, indent=4))

# Get the users from the leaderboard and store them in a list
users = []
for user in leaderboard:
    users.append(user)


# Sort the leaderboard by score using bubble sort
for i in range(len(leaderboard)):
    for j in range(len(leaderboard) - i - 1):
        if leaderboard[users[j]]["score"] < leaderboard[users[j + 1]]["score"]:
            leaderboard[users[j]], leaderboard[users[j + 1]] = leaderboard[users[j + 1]], leaderboard[users[j]]


#region Print the leaderboard
fancy_print("Leaderboard:", Colours.RED, bold=False, wait_time=0.5)

fancy_print("Name".center(20) + "|    " + "Score".center(5), Colours.RED, bold=True, wait_time=0.2)
for name in leaderboard:
    fancy_print(name.center(20) + "|    " + str(leaderboard[name]["score"]).center(5), Colours.RED, bold=False, wait_time=0.5)

#endregion Print the leaderboard

#endregion Leaderboard - Initialisation

#region User - Initialisation
while True:
    try:
        # Try to get the user's name and turn it into a string
        user_name = str(fancy_input("What is your name? ", Colours.GREEN, True, wait_time=0.5))
        break
    except ValueError:
        # If the user's name is not a string, print an error message
        fancy_print("Please enter a valid name", Colours.RED, True, wait_time=0.5)


# Has the user played before?
if user_name in leaderboard:
    # If the user has played before, print a welcome back message
    fancy_print("Welcome back " + user_name + "!", Colours.BLUE , True, wait_time=0.5)

    # Check if the user has the correct password
    while True:
        try:
            # Try to get the user's password and turn it into a string
            user_password = str(fancy_input("What is your password? ", Colours.GREEN, True, wait_time=0.5))
            break
        except ValueError:
            # If the user's password is not a string, print an error message
            fancy_print("Please enter a valid password", Colours.RED, True, wait_time=0.5)

    # Check if the user's password is correct
    if user_password == leaderboard[user_name]["password"]:
        # If the user's password is correct, print a success message
        fancy_print("Password correct!", Colours.GREEN, True, wait_time=0.5)

        # Check if the user wants to change their password
        while True:
            try:
                # Try to get the user's answer and turn it into a string
                change_password = str(fancy_input("Do you want to change your password? (y/n) ", Colours.GREEN, True, wait_time=0.5))
                break
            except ValueError:
                # If the user's answer is not a string, print an error message
                fancy_print("Please enter a valid answer", Colours.RED, True, wait_time=0.5)



        # Check if the user wants to change their password
        if change_password == "y":
            # If the user wants to change their password, ask them for their new password
            while True:
                try:
                    # Try to get the user's new password and turn it into a string
                    new_password = str(fancy_input("What is your new password? ", Colours.GREEN, True, wait_time=0.5))
                    break
                except ValueError:
                    # If the user's new password is not a string, print an error message
                    fancy_print("Please enter a valid password", Colours.RED, True, wait_time=0.5)

            # Change the user's password
            leaderboard[user_name]["password"] = new_password
            # Print a success message
            fancy_print("Password changed!", Colours.GREEN, True, wait_time=0.5)

        # Check if the user wants to play the game
        while True:
            try:
                # Try to get the user's answer and turn it into a string
                play_game = str(fancy_input("Do you want to play the game? (y/n)  > ", Colours.GREEN, True, wait_time=0.5))
                break
            except ValueError:
                # If the user's answer is not a string, print an error message
                fancy_print("Please enter a valid answer", Colours.RED, True, wait_time=0.5)

        # Check if the user wants to play the game
        if play_game == "y":
            # If the user wants to play the game, print a success message
            fancy_print("Let's play!", Colours.GREEN, True, wait_time=0.5)

        else:
            # If the user does not want to play the game, print a goodbye message
            fancy_print("Goodbye!", Colours.GREEN, True, wait_time=0.5)
            # Exit the program
            exit()

    else:
        # If the user's password is incorrect, print an error message
        fancy_print("Password incorrect!", Colours.RED, True, wait_time=0.5)
        # Exit the program
        exit()
else:
    # If the user has not played before, print a welcome message
    fancy_print("Welcome " + user_name + "!", Colours.BLUE , True, wait_time=0.5)

    # Get the user's password
    while True:
        try:
            # Try to get the user's password and turn it into a string
            user_password = str(fancy_input("Enter a new password >", Colours.GREEN, True, wait_time=0.5))
            break
        except ValueError:
            # If the user's password is not a string, print an error message
            fancy_print("Please enter a valid password", Colours.RED, True, wait_time=0.5)

    # Add the user to the leaderboard
    leaderboard[user_name] = {"password": user_password, "score": "0"}
    # Print a success message
    fancy_print("User added!", Colours.GREEN, True, wait_time=0.5)

    # Check if the user wants to play the game
    while True:
        try:
            # Try to get the user's answer and turn it into a string
            play_game = str(fancy_input("Do you want to play the game? (y/n)  > ", Colours.GREEN, True, wait_time=0.5))
            break
        except ValueError:
            # If the user's answer is not a string, print an error message
            fancy_print("Please enter a valid answer", Colours.RED, True, wait_time=0.5)

    # Check if the user wants to play the game
    if play_game == "y":
        # If the user wants to play the game, print a success message
        fancy_print("Let's play!", Colours.GREEN, True, wait_time=0.5)

    else:
        # If the user does not want to play the game, print a goodbye message
        fancy_print("Goodbye!", Colours.GREEN, True, wait_time=0.5)
        # Exit the program
        exit()

# After all that mess above, we can save the leaderboard to leaderboard.json
with open("leaderboard.json", "w", encoding="UTF-8") as leaderboard_file:
    leaderboard_file.write(json.dumps(leaderboard, indent=4))

#endregion User - Initialisation


teachers = {
    "Mr Smith": {
        "Subject": "electronics",
        "Health": 100,
        "Attack": 10,
        "Defence": 20,
        "Ascii": """
        """
        },
    "Mr Cammack": {
        "Subject": "pe",
        "Health": 120,
        "Attack": 15,
        "Defence": 15,
        },
    "Mr Birchall": {
        "Subject": "EVERYTHING",
        "Health": 150,
        "Attack": 20,
        "Defence": 10,
        },
}

students = {
    "John": {
        "Health": 150,
        "Attack": 10,
        "Defence": 25
        },

    "Ogo": {
        "Health": 120,
        "Attack": 15,
        "Defence": 20
        },

    "Eli": {
        "Health": 100,
        "Attack": 20,
        "Defence": 15
        },

    "Thomas": {
        "Health": 80,
        "Attack": 25,
        "Defence": 10
        }
}



fancy_print("Available characters:", Colours.RED, True, wait_time=0.5)

# Print each student's name, health, attack and defence 

for student in students:
    fancy_print(student + ":", Colours.PURPLE, True, wait_time=0.5)
    fancy_print(" > Health: " + str(students[student]["Health"]), Colours.GREEN, True, wait_time=0.2)
    fancy_print(" > Attack: " + str(students[student]["Attack"]), Colours.RED, True, wait_time=0.2)
    fancy_print(" > Defence: " + str(students[student]["Defence"]), Colours.BLUE, True, wait_time=0.2)
    print()


# Ask the user which student they want to be
while True:
    try:
        # Try to get the user's answer and turn it into a string
        user_student_input = str(fancy_input("Which student do you want to be? ", Colours.GREEN, True, wait_time=0.5))


        user_student = students[user_student_input] # Set user_student to the student's stats. Should raise a KeyError if the user's answer is not a valid student
        # If the user's answer is a valid student, print a success message
        fancy_print("You are now " + user_student_input + "!", Colours.GREEN, True, wait_time=0.5)
        break

    except ValueError:
        # If the user's answer is not a string, print an error message
        fancy_print("Please enter a valid student!", Colours.RED, True, wait_time=0.5)
    except KeyError:
        # If the user's answer is not a valid student, print an error message
        fancy_print("Please enter a valid student!", Colours.RED, True, wait_time=0.5)


user_score = 0
def main_game_loop():
    # Main game loop. 

    # Print player's health, attack and defence and score

    fancy_print("Your stats:", Colours.RED, True, wait_time=0.5)
    fancy_print(" > Health: " + str(user_student["Health"]), Colours.GREEN, True, wait_time=0.2)
    fancy_print(" > Attack: " + str(user_student["Attack"]), Colours.RED, True, wait_time=0.2)
    fancy_print(" > Defence: " + str(user_student["Defence"]), Colours.BLUE, True, wait_time=0.2)
    fancy_print(" > Score: " + str(user_score), Colours.PURPLE, True, wait_time=0.2)
    print()


    # Randomly choose a teacher
    teacher_name = random_choice(list(teachers.keys()))
    teacher_stats = teachers[teacher_name]

    # Print the teacher's name, health, attack and defence
    fancy_print(f"{teacher_name} has appeared!", Colours.RED, True, wait_time=0.5)
    fancy_print(" > Health: " + str(teacher_stats["Health"]), Colours.GREEN, True, wait_time=0.2)
    fancy_print(" > Attack: " + str(teacher_stats["Attack"]), Colours.RED, True, wait_time=0.2)
    fancy_print(" > Defence: " + str(teacher_stats["Defence"]), Colours.BLUE, True, wait_time=0.2)
    print()

    # Ask the user what they want to do
    while True:




        try:
            # Try to get the user's answer and turn it into a string
            user_action = str(fancy_input("What do you want to do? (attack, run) ", Colours.GREEN, True, wait_time=0.5))
            if user_action not in ["attack", "run"]:
                # If the user's answer is not a valid action, raise a ValueError
                raise ValueError 
            break

        except ValueError:
            # If the user's answer is not a string, print an error message
            fancy_print("Please enter a valid action!", Colours.RED, True, wait_time=0.5)


    if user_action == "attack":
        student_to_teacher_damage = user_student["Attack"] - teacher_stats["Defence"] + randint(-10, 10) # Add some randomness to the damage done
        teacher_to_student_damage = teacher_stats["Attack"] - user_student["Defence"] + randint(-10, 10) # Add some randomness to the damage done


        # Print the damage done to the teacher
        fancy_print("You did " + str(student_to_teacher_damage) + " damage to " + teacher_name + "!", Colours.GREEN, True, wait_time=0.5)

        # Print the damage done to the student
        fancy_print(teacher_name + " did " + str(teacher_to_student_damage) + " damage to you!", Colours.RED, True, wait_time=0.5)

        teacher_stats["Health"] -= student_to_teacher_damage
        user_student["Health"] -= teacher_to_student_damage

        # Check if the teacher's health is less than or equal to 0
        if teacher_stats["Health"] <= 0:
            # If the teacher's health is less than or equal to 0, print a success message
            fancy_print("You killed " + teacher_name + "!", Colours.GREEN, True, wait_time=0.5)
            user_score += 1
            teachers.pop(teacher_name)
            break

        # Check if the student's health is less than or equal to 0
        if user_student["Health"] <= 0:
            # If the student's health is less than or equal to 0, print a failure message
            fancy_print("You died!", Colours.RED, True, wait_time=0.5)
            break

    else:
        # If the user wants to run, print a message
        fancy_print("You ran away!", Colours.GREEN, True, wait_time=0.5)
        user_score -= 1
        

while True:
    try:
        # Try to run the main game loop
        main_game_loop()
    except KeyboardInterrupt:
        # If the user presses Ctrl+C, print a goodbye message
        fancy_print("Goodbye!", Colours.GREEN, True, wait_time=0.5)
        break

# Print the user's score
fancy_print("Your score is " + str(user_score), Colours.GREEN, True, wait_time=0.5)

# Check if the user's score is greater than the lowest score on the leaderboard
if user_score > leaderboard[user_name]["score"]:
    fancy_print("You beat your high score!", Colours.GREEN, True, wait_time=0.5)
    # If the user's score is greater than the lowest score on the leaderboard, print a success message
    fancy_print("You made it onto the leaderboard!", Colours.GREEN, True, wait_time=0.5)

    # Add the user to the leaderboard
    leaderboard[user_name] = {"password": user_password, "score": user_score}
    # Print a success message
    fancy_print("User added!", Colours.GREEN, True, wait_time=0.5)
    
else:
    # If the user's score is not greater than the lowest score on the leaderboard, print a failure message
    fancy_print("You did not make it onto the leaderboard!", Colours.RED, True, wait_time=0.5)

# We can now save the leaderboard to leaderboard.json
with open("leaderboard.json", "w", encoding="UTF-8") as leaderboard_file:
    leaderboard_file.write(json.dumps(leaderboard, indent=4))

# Print a goodbye message
fancy_print("Goodbye!", Colours.GREEN, True, wait_time=0.5)


