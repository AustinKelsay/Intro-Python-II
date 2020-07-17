from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.



# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player("Austin", room["outside"])
room["foyer"].items = ["machete", "sword"]

while True:
    print("\n")
    print(player.location)
    userDirection = input("\nEnter (n), (s), (e), (w), (d), (i) for inventory")
    userAction = input("\nEnter take [item], or drop [item]").split()
    if userDirection:
        if userDirection == "q":
            playerTurn = False
        elif userDirection == "n":
            player.move(userDirection)
        elif userDirection == "e":
            player.move(userDirection)
        elif userDirection == "s":
            player.move(userDirection)
        elif userDirection == "w":
            player.move(userDirection)
        elif userDirection == "i":
            print(player.inventory)
    if userAction:
        if "take" in userAction:
            for item in player.location.items:
                if item == userAction[1]:
                    player.takeItem(item)
                    print(player.inventory)

        if "drop" in userAction:
            for item in player.location.items:
                if item == userAction[1]:
                    player.dropItem(item)
                    print(player.inventory)



