import random

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {} # to mimic a real social network
        self.friendships = {} # acts as adjacency list

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
            # total friendships to create = avg_friendships * num_users = around 20
            # create a list with all possible friendships
        total_friendships = avg_friendships*num_users
        friendship_pairs = []

        for user_id in range(1, num_users + 1):
            for friend_id in range(user_id + 1, num_users + 1):
                friendship_pairs.append((user_id, friend_id))

        # shuffle friendships
        self.fisher_yates_shuffle(friendship_pairs)

        # grab first N elements from list
        friendships_to_make = friendship_pairs[:(total_friendships//2)]

        for friendship in friendships_to_make:
            self.add_friendship(friendship[0], friendship[1])

    def get_neighbors(self, user_id):
        return self.friendships[user_id]

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        NOTES:
            - Seems like the ideal solution will be BFT for SHORTEST PATH
        """
        # can use dictionary to keep track of visited user and.... their path?
        # friendships is kept in adjacency list form
        # graph problems: create graph, create get neighbors, create search method

        q = Queue()
        visited = {}

        q.enqueue([user_id])

        while q.size() > 0:
            current_path = q.dequeue()
            current_node = current_path[-1]

            if current_node not in visited:
                visited[current_node] = current_path

                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    path_copy = current_path + [neighbor]
                    q.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    num_users = 1000
    avg_friendships = 5
    sg.populate_graph(num_users, avg_friendships)
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # print(connections)


    # percentage of other users in extended social network
        # num of people we visited / total num of people
    
    print(len(connections)/num_users)

    # average degree of separation ---> avg steps we took to visit someone
        # average the length of each path
        # ie. how many friends do we need to go through to meet someone??
    
    total_path_lengths = 0
    for key, value in connections.items():
        total_path_lengths += len(value)

    avg_path_length = total_path_lengths/len(connections)
    print(avg_path_length)
        