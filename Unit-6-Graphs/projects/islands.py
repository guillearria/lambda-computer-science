"""
Write a function that returns the number of islands from a 2D array
    - Island = 1s that are connected n, s, e, or w
    - For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4

1. Describe the problem in graph terms:
    - What are our nodes?
        - Each (x,y) in the array
    - What are our edges?
        - Connected with a direct neighbor is a 1
    - What is an island in graph terms
        - Connected component, ie. group of 1s

2. Build your graph or write getNeighbors

3. Choose your technique(s)
    - How can we count number of connected components?
        - Traverse through array, get to an island and traverse neighbors, repeat
            - Keep track of visited 1s
"""

def island_counter(islands):
    pass



islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))