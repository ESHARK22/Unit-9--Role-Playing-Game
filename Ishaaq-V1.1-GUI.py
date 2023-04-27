# This should have been in the md file, but I forgot to add it. so now my notes are all here :)

# Game ideas:
# Enemy are teachers which ask you speicic questions based on what they teach
# Start with a simple question, then get harder
# -> KS1 -> KS2 -> KS3 -> KS4 

# add save feature

# -------------Multiplayer----------------
# How do i do mulplayer?
# -> Have a server that runs the "map" and processes all the data
# -> Have a client that connects to the server
# -> client should NOT be P2P (cheating, ip leask etc.)
# Lag? future me will deal with that. I should probably think this through more.

# -> Have a client that connects to the server
    # What would gameplay be like?
    # -> Players can fight each other
    # -> Players can fight teachers to level up
    # -> Players can ask each other questions
    # -> Players can trade "items"


class Player:
    def __init__(self) -> None:
        pass

    health = 100
    attack = 10
    defence = 10
    speed = 10
    remaining_sprint = 10
    inventory = []
    
    def attack(self, enemy):
        print(f"You attack the enemy {enemy}")

    def recieve_damage(self, damage):
        self.health -= damage
        print(f"You recieve {damage} damage")

    def heal(self, amount):
        self.health += amount
        print(f"You heal {amount} health")

    def sprint(self):
        self.remaining_sprint -= 1
        print("You sprinted")

    def walk(self):
        print("You walk")

    def use_item(self, item):
        print(f"You use the item {item}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"You add the item {item} to your inventory")

    def remove_item(self, item):
        self.inventory.remove(item)
        print(f"You remove the item {item} from your inventory")


class Item:
    executor = str # What to run when the item is used
    name = str
    description = str
    


class Enemy:

    pass



player = Player()

while True:

    user_input = input("What do you want to do? ")

    if user_input == "attack":
        