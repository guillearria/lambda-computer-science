'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Attempt 1
    # loop through arr, get i
        # pop item at that i
        # check if pop value is in arr
        # return pop value if yes
    # dup_arr = arr.copy()
    # for num in arr:
    #     dup_arr.remove(num)
    #     if num not in dup_arr:
    #         return num

    # Attempt 2, inefficient
    # init count dictionary
    # loop through arr, nums
        # if num  in keys, add to count
        # else, create new key with val 1
    # look for min value of dictionary, return key

    # Attempt 3
    # init set of arr
    # loop through set
        # remove num from arr
        # if num not in arr, return num
    dups_removed = set(arr)
    for num in dups_removed:
        arr.remove(num)
        if num not in arr:
            return num

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")