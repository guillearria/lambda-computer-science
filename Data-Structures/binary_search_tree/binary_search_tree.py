"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

* Rule: Each vertex (node) has single inbound edge (parent)
* Rule: Each vertex (node) has no more than two children
* Rule: Values less than a node are stored in LEFT subtree
* Rule: Values greater than or equal to a node are stored in RIGHT subtree

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value): 
        # ITERATIVE
        # while not at bottom of tree
            # if value < root node, go left
                # if left child is None
                    # add here
                    # exit loop
            # if value >= root node, go right
                # if right child is None
                    # add here
                    # exit loop

        # RECURSIVE
        # if value < root node
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # if value >= root node
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # recursive call
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # RECURSIVE
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            elif self.left.value == target:
                return True
            else:
                self.left.contains(target)
        else:
            if self.right is None:
                return False
            elif self.right.value == target:
                return True
            else:
                self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # return value at far right
        if self.right is None:
            return self.value
        else:
            cur_node = self.right
            while cur_node.right is not None:
                cur_node = cur_node.right
            return cur_node.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # create a queue for nodes
        # add the first node to the queue
        
        # while queue is not empty
        #     remove the first node from the queue
        #     print the removed node
        #     add all children of that node into the queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # V1
        # if self.left:
        #     self.left.in_order_print()
        # print(self.value)
        # if self.right:
        #     self.right.in_order_print()

        # create a stack to keep track of nodes we are processing
        # push 'self' into stack

        # while something is in stack (not done processing all nodes)
            # use existing for_each() as a reference for traversal logic
            # push when we START processing a node, pop when node is done
            # don't forget to call print
            
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()


    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
