# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)

# def earliest_ancestor(ancestors, starting_node):
#     """
#     ancestors - list of parent/child nodes
#     starting_node - node of child
#     """
#     # convert pairs to adjacency list, child (1) to parent (0)
#     vertices = {}

#     # add vertices and edges
#     for pair in ancestors:
#         vertices[pair[0]] = set()
#         vertices[pair[1]] = set()

#     for pair in ancestors:
#         vertices[pair[1]].add(pair[0])

#     # solve with BFS
#     q = Queue()
#     q.enqueue([starting_node])
#     visited = set()
#     possible_ancestors = {}
#     level = 0

#     while q.size() > 0:
#         current_path = q.dequeue()
#         current_node = current_path[-1]

#         if current_node not in visited: # can be removed
#             visited.add(current_node)

#             neighbors = vertices[current_node]
#             if len(neighbors) == 0:
#                 if level in possible_ancestors:
#                     possible_ancestors[level].append(current_node)
#                 else:
#                     possible_ancestors[level] = [current_node]
#             else:
#                 for neighbor in neighbors:
#                     path_copy = current_path + [neighbor]
#                     q.enqueue(path_copy)
            
#             level += 1

#     if starting_node in sum(possible_ancestors.values(), []):
#         return -1
#     else:
#         max_level = max(possible_ancestors)
#         return min(possible_ancestors[max_level])

"""
FROM CLASS:

This is DAG problem, directed acyclic graph that requires a traversal
    - Should be though about child to parent direction
    - Can use either BFS or DFS
"""
# NEEDS GET NEIGHBORS FUNCTION
def getNeighbors(node):
    pass

# RECURSIVE with DFT to track distance
def dft(ancestors, node, distance):
    parents = getNeighbors(node)

    if len(parents) == 0:
        return (node, distance)

    ancient_one = (node, distance)
    for parent in parents:
        node_pair = dft(ancestors, parent, distance + 1)

        if node_pair[1] > distance:
            ancient_one = node_pair

    # MISSING: if earliest ancestor returned is == starting node, return -1

    return ancient_one

def earliest_ancestor(ancestors, starting_node):
    ancient_one = dft(ancestors, starting_node, 0)

    return ancient_one
