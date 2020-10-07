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

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")