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


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")