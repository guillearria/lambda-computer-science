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

# Dramatic print


def steady_print(text):
    for character in text:
        sys.stdout.write(character)
        time.sleep(.05)
    return ""

# Clear terminal screen


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

#
# Main
#


def start_game():
    def display_location(loc):
        print(steady_print(f"Current location: {loc.name}"))
        print(loc.description)
        print("")
        print(steady_print(f"Items available here: {loc.items}"))
        print("")

    def choose_action(room):
        available_rooms = {
            "n": room.n_to,
            "s": room.s_to,
            "e": room.e_to,
            "w": room.w_to
        }

        while True:
            choice = input(
                "What would you like to do?\n[n, s, e, w or <take, get, drop> item]: ")
            print("")
            word_ct = len(choice.split(" "))
            if choice == "q":
                print(steady_print("Game Over!"))
                print("")
                quit()
            elif word_ct == 1:
                next_room = available_rooms[choice]
                if next_room:
                    nonlocal p1
                    p1.current_room = next_room
                    return ""
                else:
                    print(steady_print(
                        f"You can't go in this direction so you return to the {room.name}..."))
                    print("")
            elif word_ct == 2:
                print(f"{choice}")
                print("")
            else:
                print(steady_print("Unknown command..."))
                print("")

    cls()
    player_name = input("Enter your name: ")
    p1 = Player(player_name, room["outside"])

    print("")
    print(steady_print(f"Welcome treasure hunter, {p1.name}!"))
    print(steady_print("Enter 'q' during any input to exit game.."))
    print("")

    while True:
        current_room = p1.current_room
        display_location(current_room)
        choose_action(current_room)


if __name__ == '__main__':
    start_game()
