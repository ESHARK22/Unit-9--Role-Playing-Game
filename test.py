rooms = {
    "Room1":{
        "rooms": ["Room2","Room3"],
        "Boss": "Boss1"
    },
    "Room2":{
        "rooms": ["Room1","Room3"],
        "Boss": "Boss2"
    },
    "Room3":{
        "rooms": ["Room1"],
        "Boss": "Boss3",
    }
}
room = "Room1"

while True:
    print("You are in",room)
    print("You can go to:")
    for r in rooms[room]:
        print(r)

    choice = input("Where do you want to go? ")
    if choice in rooms[room]:
        room = choice
    else:
        print("You can't go there")