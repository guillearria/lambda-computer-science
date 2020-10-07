'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Attempt 1: did not work because of negatives
    # sort list
    # reverse it
    # arr = sorted(arr)
    # arr.reverse()
    # return arr

    # Attempt 2:
    # create new list
    # loop through arr
    # if num is not zero, add to list, remove from arr
    # add remaining arr to new list
    zero_arr = []
    num_arr = []
    for num in arr:
        if num != 0:
            num_arr.append(num)
        else:
            zero_arr.append(num)

    num_arr.extend(zero_arr)
    return num_arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")