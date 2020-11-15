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

def earliest_ancestor(ancestors, starting_node):
    """
    ancestors - list of parent/child nodes
    starting_node - node of child
    """
    # convert pairs to adjacency list, child (1) to parent (0)
    vertices = {}

    # add vertices and edges
    for pair in ancestors:
        vertices[pair[0]] = set()
        vertices[pair[1]] = set()

    for pair in ancestors:
        vertices[pair[1]].add(pair[0])

    # solve with BFS
    q = Queue()
    q.enqueue([starting_node])
    visited = set()
    possible_ancestors = {}
    level = 0

    while q.size() > 0:
        current_path = q.dequeue()
        current_node = current_path[-1]

        if current_node not in visited:
            visited.add(current_node)

            neighbors = vertices[current_node]
            if len(neighbors) == 0:
                if level in possible_ancestors:
                    possible_ancestors[level].append(current_node)
                else:
                    possible_ancestors[level] = [current_node]
            else:
                for neighbor in neighbors:
                    path_copy = current_path + [neighbor]
                    q.enqueue(path_copy)
            
            level += 1

    if starting_node in sum(possible_ancestors.values(), []):
        return -1
    else:
        max_level = max(possible_ancestors)
        return min(possible_ancestors[max_level])