import sys
import os
import time
import textwrap
from room import Room
from player import Player

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


def steady_print(text):
    for character in text:
        sys.stdout.write(character)
        time.sleep(.05)
    return ""

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#
# Main
#
def start_game():
    def display_location(loc):
        print("")
        print(steady_print(f"Current location: {loc.name}"))
        print(steady_print(loc.description))
        print("")
        print(steady_print(f"Items available: {loc.items}"))

    def outside_choice():
        options = ["y", "n"]
        choice = ""
        while choice not in options:
            choice = input("Do you dare enter the cave? [y, n]: ")
            print("")
            if choice == "y":
                nonlocal p1
                p1.current_room = room["foyer"]
                return steady_print("You take a deep breath and enter...\n")
            elif choice == "n":
                print(steady_print("Game Over."))
                quit()
            elif choice == "q":
                print(steady_print("Game Over."))
                quit()
            else:
                print(steady_print("I didn't understand that."))

    def in_cave_choice(location):
        rooms = {
            "n": location.n_to,
            "s": location.s_to,
            "e": location.e_to,
            "w": location.w_to
        }

        while True:
            choice = input("Which way do you go? [n, s, e, w]: ")
            if choice == "q":
                print(steady_print("\nGame Over."))
                quit()
            else:
                next_room = rooms[choice]

            if next_room:
                nonlocal p1
                p1.current_room = next_room
                return ""
            else:
                print(steady_print(
                    f"\nYou can't go in this direction so you return to the {location.name}...\n"))

    cls()
    print(steady_print("Welcome treasure hunter!"))
    player_name = input("Enter your name: ")
    
    print(steady_print("\nEnter 'q' during any input to exit game."))

    p1 = Player(player_name, room["outside"])

    while True:
        location = p1.current_room
        if location.name == room["outside"].name:
            display_location(location)
            outside_choice()
        else:
            display_location(location)
            in_cave_choice(location)


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

if __name__ == '__main__':
    start_game()
