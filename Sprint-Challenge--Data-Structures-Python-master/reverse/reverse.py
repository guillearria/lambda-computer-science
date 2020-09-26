class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head is None:
            return
        elif self.head.next_node is None:
            return
        else: 
            # prev_node = node
            # cur_node = node
            # while cur_node.next_node is not prev:
            #     prev_node = cur_node
            #     cur_node = cur_node.next_node
            # cur_node.set_next(prev_node)
            # self.reverse_list(prev_node, cur_node)
            node_list = []
            cur_node = node
            while cur_node is not None:
                node_list.append(cur_node)
                cur_node = cur_node.next_node
            node_list.reverse()
            self.head = node_list[0]
            for i, n in enumerate(node_list):
                if i+1 < len(node_list):
                    n.set_next(node_list[i+1])
                else:
                    n.set_next(None)
