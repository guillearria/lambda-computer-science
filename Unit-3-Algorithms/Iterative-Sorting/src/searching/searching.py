def linear_search(arr, target):
    # Given a set of data, traverse the dataset one item 
    # at a time until either you find the item you are 
    # looking for OR check every item in the set and verify 
    # the item you are looking for is not there.
    for i, item in enumerate(arr):
        if item == target:
            return i

    return -1   # not found

# from class
def insertion_sort(a):    # "In-place", does not allocate a new array
    for i in range(1, len(a)):
        val = a[i]
        j = i

        while j > 0 and val < a[j - 1]:
            a[j], a[j-1] = a[j-1], a[j]  # swap
            j -= 1

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # test already sorted but for other applications:
    # insertion_sort(arr)
        
    # Compare middle item to target
    # if its the same, stop
    # if target < middle item, eliminate RHS, search LHS
    # if target > middle item, eliminate LHS, search RHS
    dup_arr = arr.copy()
    while len(dup_arr): 
        middle_index = (len(dup_arr)-1)//2
        middle_value = dup_arr[middle_index]
        if middle_value == target:
            return arr.index(middle_value)
        elif target < middle_value:
            dup_arr = dup_arr[0:middle_index]
        elif target > middle_value:
            dup_arr = dup_arr[middle_index+1:]


    return -1  # not found
