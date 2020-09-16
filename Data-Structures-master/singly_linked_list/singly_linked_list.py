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
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Set next_node of new_node to current head
            new_node.set_next_node(self.head)
            # Update current head to new_node
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail:
            self.head.set_next_node(new_node)
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node
    def remove_head(self):
        # Cases?
        if self.head is None:
            return None
        else:
            ret_value = self.head.get_value()
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        # TODO

    def contains(self, value):
        # TODO time permitting

    def get_max(self):
        # TODO time permitting
