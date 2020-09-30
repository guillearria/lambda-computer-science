def linear_search(arr, target):
    # Given a set of data, traverse the dataset one item 
    # at a time until either you find the item you are 
    # looking for OR check every item in the set and verify 
    # the item you are looking for is not there.
    for i, item in enumerate(arr):
        if item == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here


    return -1  # not found
