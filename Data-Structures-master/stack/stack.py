"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# 1. Using array as underlying structure
# Remove from head, add to head


# class Stack:
#     def __init__(self):
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.insert(0, value)

#     def pop(self):
#         if len(self.storage):
#             popped_element = self.storage.pop(0)
#             return popped_element
#         else:
#             return None


# 2. Using linked list as underlying structure


from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size:
            self.size -= 1
            removed_head_val = self.storage.remove_head()
            return removed_head_val
        else:
            return None


# 3. What is the difference between using an array vs. a linked list when 
# implementing a Stack?

""" The difference is not having to use self.size with an array since they come with
built-in len method. Append and pop are very similar to the add and remove methods
of a LinkedList."""