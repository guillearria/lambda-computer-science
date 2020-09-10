import sys
import os
import time
import textwrap
from room import Room
from player import Player
from item import Item

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

# Add items to rooms
room['outside'].items = [Item("torch", "still usable")]
room['foyer'].items = [Item("lighter", "barely any fluid left")]
room['overlook'].items = [Item("sword", "shiny"), Item("bow","still works")]
room['narrow'].items = [Item("arrows", "handmade bundle")]
room['treasure'].items = [Item("bones", "very old")]

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
    def display_location(player):
        current_room = player.current_room
        room_items = [item.name for item in current_room.items]
        inventory = [item.name for item in player.inventory]
        print(steady_print(f"Current location: {current_room.name}"))
        print(current_room.description)
        print("")
        print(steady_print(f"Items in this room: {room_items}"))
        print(f"Player inventory: {inventory}")
        print("")

    def update_items(player):
        current_room = player.current_room
        room_items = [item.name for item in current_room.items]
        inventory = [item.name for item in player.inventory]
        print(steady_print(f"Items in this room: {room_items}"))
        print(f"Player inventory: {inventory}")
        print("")

    def choose_action(player):
        current_room = player.current_room
        available_rooms = {
            "n": current_room.n_to,
            "s": current_room.s_to,
            "e": current_room.e_to,
            "w": current_room.w_to
        }

        while True:
            choice = input(
                "What would you like to do?\n[n, s, e, w or <take, get, drop> item]: ")
            print("")
            word_split = choice.split(" ")
            word_ct = len(word_split)
            if choice == "q":
                print(steady_print("Game Over!"))
                print("")
                quit()
            elif word_ct == 1:
                valid_choices = ['n', 's', 'e', 'w']
                if choice in valid_choices:
                    next_room = available_rooms[choice]
                    if next_room:
                        player.current_room = next_room
                        return ""
                    else:
                        print(steady_print(
                            f"You can't go in this direction..."))
                        print("")
                else:
                    print(steady_print("Unknown command..."))
                    print("")
            elif word_ct == 2:
                verb_choice = word_split[0]
                item_choice = word_split[1]
                if verb_choice == "take" or verb_choice == "get":
                    room_items = current_room.items
                    item_names = [item.name for item in room_items]
                    if item_choice in item_names:
                        item = room_items[item_names.index(item_choice)]
                        item.on_take()
                        current_room.remove_item(item)
                        player.add_item(item)
                        update_items(player)
                    else:
                        print(steady_print(
                            f"There's no {item_choice} in this room.."))
                        print("")
                elif verb_choice == "drop":
                    inventory = player.inventory
                    item_names = [item.name for item in inventory]
                    if item_choice in item_names:
                        item = inventory[item_names.index(item_choice)]
                        item.on_drop()
                        current_room.add_item(item)
                        player.remove_item(item)
                        update_items(player)
                    else:
                        print(steady_print(
                            f"There's no {item_choice} in your inventory.."))
                        print("")
                else:
                    print(steady_print(f"Unable to {choice}!"))
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
        display_location(p1)
        choose_action(p1)


if __name__ == '__main__':
    start_game()
