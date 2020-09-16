class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_node):
        self.next_node = new_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # Create new node
        new_node = Node(value)

        # Set next_node of new_node to current head
        new_node.set_next_node(self.head)

        # Update current head to new_node
        self.head = new_node

    def add_to_tail(self, value):
        # TODO

    def remove_head(self):
        # TODO

    def remove_tail(self):
        # TODO

    def contains(self, value):
        # TODO time permitting

    def get_max(self):
        # TODO time permitting