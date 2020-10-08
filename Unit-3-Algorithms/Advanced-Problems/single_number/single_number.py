'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
import time
import random

def single_number(arr):
    start = time.perf_counter()
    # First pass solution:
        # Time complexity: O(n^2)
        # Space complexity: 

    # init set of arr
    # loop through set
        # remove num from arr
        # if num not in arr, return num

    # dups_removed = set(arr)
    # for num in dups_removed:
    #     arr.remove(num)
    #     if num not in arr:
    #         end = time.perf_counter()
    #         print("Runtime:", end-start, "seconds")
    #         return num

    # Optimized solution:
        # how can we keep track of duplicates?
        # use hash table
            # {
            #   signature: [duplicates]
            # }

    result = {}

    for num in arr:
        signature = num
        if signature not in result:
            result[signature] = 1
        else:
            del result[signature]

    end = time.perf_counter()
    print("Runtime:", end-start, "seconds")
    # next, iter faster than list()
    return next(iter(result))

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    random.shuffle(arr)

    print(f"The odd-number-out is {single_number(arr)}")