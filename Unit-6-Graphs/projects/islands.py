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

# GET NEIGHBORS FUNC


def getNeighbors(row, col, matrix):
    neighbors = []

    if col >= 1:
        west = matrix[row][col - 1]
        if west == 1:
            neighbors.append((row, col - 1))

    if col <= len(matrix) - 2:
        east = matrix[row][col + 1]
        if east == 1:
            neighbors.append((row, col + 1))

    if row <= len(matrix) - 2:
        south = matrix[row + 1][col]
        if south == 1:
            neighbors.append((row + 1, col))

    if row >= 1:
        north = matrix[row - 1][col]
        if north == 1:
            neighbors.append((row - 1, col))

    return neighbors

# TRAVERSAL FUNC


def dft_recursive(row, col, visited, matrix):
    if (row, col) not in visited:
        visited.add((row, col))

        neighbors = getNeighbors(row, col, matrix)

        for neighbor in neighbors:
            dft_recursive(neighbor[0], neighbor[1], visited, matrix)


def island_counter(matrix):
    # iterate over matrix:
        # if 0, continue
        # if 1, traverse neighbors, add to visited, continue iteration

    visited = set()
    conn_component_count = 0

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            node = matrix[row][col]

            if node == 0:
                continue
            elif node == 1:
                if (row, col) not in visited:
                    conn_component_count += 1
                    dft_recursive(row, col, visited, matrix)

    return conn_component_count


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))
