"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        vertices = self.vertices.keys()
        if v1 in vertices and v2 in vertices:
            self.vertices[v1].add(v2)
        else:
            raise Exception("One or more vertices not found!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # check every node/connection ONCE
        # keep track with visited set
        # use QUEUE for BFT

        queue = Queue()
        queue.enqueue(starting_vertex)

        visited = set()  # better than list, O(1)

        while queue.size() > 0:
            cur_node = queue.dequeue()
            if cur_node not in visited:
                print(cur_node)
                visited.add(cur_node)

                neighbors = self.get_neighbors(cur_node)
                for neighbor in neighbors:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # check every node/connection ONCE
        # keep track with visited set
        # use STACK for BFT
        # put starting vertex on top of stack
        # while stack is NOT empty
        # pop off top of stack (starting vertex), cur node
        # check if we have visited this node
        # if not, add it to visited set and print
        # also add each of its neighbors into stack

        stack = Stack()
        stack.push(starting_vertex)

        visited = set()

        while stack.size() > 0:
            cur_node = stack.pop()
            if cur_node not in visited:
                print(cur_node)
                visited.add(cur_node)

                neighbors = self.get_neighbors(cur_node)
                for neighbor in neighbors:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # needs base case
        # also needs to be able to call itself, add visited set to vars

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)

            neighbors = self.get_neighbors(starting_vertex)
            if len(neighbors) == 0:
                return
            else:
                for n in neighbors:
                    self.dft_recursive(n, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)

        paths = [[starting_vertex]]
        prev_path_idx = 0

        visited = set()

        while queue.size() > 0:
            cur_node = queue.dequeue()
            if cur_node not in visited:
                visited.add(cur_node)
                neighbors = self.get_neighbors(cur_node)
                for neighbor in neighbors:
                    new_path = paths[prev_path_idx].copy()
                    new_path.append(neighbor)
                    if neighbor == destination_vertex:
                        return new_path
                    else:
                        paths.append(new_path)
                        queue.enqueue(neighbor)

                prev_path_idx += 1

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # enqueue PATHS instead of single vertex
        # during neighbors loop, make path copy and add to existing path

        stack = Stack()
        stack.push(starting_vertex)

        paths = {starting_vertex: [starting_vertex], }

        visited = set()

        while stack.size() > 0:
            cur_node = stack.pop()
            if cur_node not in visited:
                visited.add(cur_node)
                neighbors = self.get_neighbors(cur_node)
                for neighbor in neighbors:
                    new_path = paths[cur_node].copy()
                    new_path.append(neighbor)
                    if neighbor == destination_vertex:
                        return new_path
                    else:
                        paths[neighbor] = new_path
                        stack.push(neighbor)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), paths={}):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if len(visited) == 0:
            paths = {starting_vertex: [starting_vertex]}

        if starting_vertex not in visited:
            visited.add(starting_vertex)

            neighbors = self.get_neighbors(starting_vertex)
            if len(neighbors) == 0:
                return 
            else:
                for neighbor in neighbors:
                    new_path = paths[starting_vertex].copy()
                    new_path.append(neighbor)
                    if neighbor == destination_vertex:
                        print('found!', new_path)
                        return new_path
                    else:
                        paths[neighbor] = new_path
                        print(paths)
                        self.dfs_recursive(neighbor, destination_vertex, visited, paths)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
