from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt" # REQUIRED FOR PASSING

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

""" 
PLANNING:
    - Player always starts at room 0
    - Goal: player musttravel every room at least once and find shortest path (BFS?)
    - start at 0, select random unexplored, keep track of graph AND path
    - repeat until you hit none unexplored, then return the same way you came
    - look for more unexplored
    - when graph reaches 500 entries, player is done 

Useful commands: 
    -`player.current_room.id` ==
    -`player.current_room.get_exits()` == get neighbors
    -`player.travel(direction)` 
"""

# START HERE
# initiate graph
# add starting room and its unexplored exits
# choose a random unexplored room, defined by a val of None

visited = {}


def opposite_dir(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'


while len(visited) < len(room_graph):
    cur_room = player.current_room.id
    possible_exits = player.current_room.get_exits()

    if cur_room not in visited:
        visited[cur_room] = {direction: None for direction in possible_exits}

    direction = next(
        (direction for direction in possible_exits if visited[cur_room][direction] is None), None)

    if direction:
        print(f'going {direction}')
        player.travel(direction)
        nxt_room = player.current_room.id
        traversal_path.append((direction, cur_room))
        visited[cur_room][direction] = nxt_room

        possible_exits = player.current_room.get_exits()
        if nxt_room not in visited:
            visited[nxt_room] = {
                direction: None for direction in possible_exits}
        visited[nxt_room][opposite_dir(direction)] = cur_room
    else:
        print(f'--> dead end, current room {cur_room}')
        reverse_path = []

        destination_room = next(
            (room for room in visited if None in visited[room].values()), None)
        print(f'--> nearest room w unexplored exit: {destination_room}')

        q = Queue()

        possible_paths = {}
        q.enqueue(cur_room)

        while q.size() > 0:
            temp_cur_room = q.dequeue()
            possible_exits = visited[temp_cur_room]

            if temp_cur_room == destination_room:
                path_to_dest = possible_paths[temp_cur_room]
                break

            for direction, next_room in possible_exits.items():
                if next_room is not None:
                    if next_room != temp_cur_room:
                        if len(possible_paths) == 0:
                            temp_path = []
                        else:
                            temp_path = possible_paths[temp_cur_room]
                        possible_paths[next_room] = temp_path + [direction]
                        q.enqueue(next_room)

        for direction in path_to_dest:
            cur_room = player.current_room.id
            traversal_path.append((direction, cur_room))
            print(f'going {direction}')
            player.travel(direction)

traversal_path = [pair[0] for pair in traversal_path]


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
