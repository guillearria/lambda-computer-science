"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# 1. Using array as underlying structure
# Remove from head, add to tail


# class Queue:
#     def __init__(self):
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage):
#             popped_element = self.storage.pop(0)
#             return popped_element
#         else:
#             return None


# 2. Using linked list as underlying structure


# from singly_linked_list import LinkedList


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.add_to_tail(value)

#     def dequeue(self):
#         if self.size:
#             self.size -= 1
#             removed_head_val = self.storage.remove_head()
#             return removed_head_val
#         else:
#             return None


# 3. What is the difference between using an array vs. a linked list when
# implementing a Queue?

""" The difference is not having to use self.size with an array since it comes with
built-in len method. Append and pop are also very similar to the add and remove methods
of a LinkedList."""

# 4. Stretch: What if you could only use instances of your Stack class to implement the Queue?
# What would that look like? How many Stacks would you need? Try it!


from stack import Stack


class Queue:
    def __init__(self):
        self.storage = Stack()

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.size += 1
        self.storage.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.pop()