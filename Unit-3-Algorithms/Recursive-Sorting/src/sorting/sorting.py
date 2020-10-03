# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # initialize empty array
    merged_arr = []

    # keep track of where we are in each array
    indexA = 0
    indexB = 0

    # go through both copies until we run out of elements
    while indexA < len(arrA) and indexB < len(arrB):
        # if arrA has smaller element, append to sorted, update pointer
        if arrA[indexA] <= arrB[indexB]:
            merged_arr.append(arrA[indexA])
            indexA += 1
        else:
            merged_arr.append(arrB[indexB])
            indexB += 1

    # if we run out of one list, continue with other list
    while indexA < len(arrA):
        merged_arr.append(arrA[indexA])
        indexA += 1
    while indexB < len(arrB):
        merged_arr.append(arrB[indexB])
        indexB += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    start = 0
    end = len(arr)
    mid = (start+end)//2
    a = merge_sort(arr[:mid])
    b = merge_sort(arr[mid:])
    return merge(a, b)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here


# Merge sort
# ----------
# Phase 1: calling down the recursion:
#           [5 9 3 7 2 8 1 6]
#      [5 9 3 7]         [2 8 1 6]
#     [5 9] [3 7]       [2 8] [1 6]
#   [5] [9] [3] [7]   [2] [8] [1] [6]
# Phase 2: merge! returning from recursion:
#   [5] [9] [3] [7]   [2] [8] [1] [6]
#     [5 9] [3 7]       [2 8] [1 6]
#      [3 5 7 9]         [1 2 6 8]
#          [1 2 3 5 6 7 8 9]
