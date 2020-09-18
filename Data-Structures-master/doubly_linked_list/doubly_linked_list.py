"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            # assign next of new head as old head
            new_node.next = self.head
            # assign prev of old head as new head
            self.head.prev = new_node
            # assign new head
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        self.length -= 1
        ret_value = self.head
        if ret_value is None:
            return None
        elif self.head == self.tail:
            self.head = self.tail = None
        else: 
            # assign next of cur head as new head
            self.head = self.head.next
            # assign new head prev as None
            self.head.prev = None
        return ret_value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            # assign old tail next as new node
            self.tail.next = new_node
            # assign new node prev as old tail
            new_node.prev = self.tail
            # assign new tail
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        self.length -= 1
        ret_value = self.head
        if self.head is None:
            return None
        elif self.head == self.tail:
            self.head = self.tail = None
        else: 
            # assign prev of cur tail as new tail
            self.tail = self.tail.prev
            # assign new tail next as None
            self.tail.next = None
        return ret_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length is None:
            return None
        elif self.head == self.tail:
            self.head = self.tail = None
        elif node is self.head:
            self.head = node.next
            self.head.prev = None

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass