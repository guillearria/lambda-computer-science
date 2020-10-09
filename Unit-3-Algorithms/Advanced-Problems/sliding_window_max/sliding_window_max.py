'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    # First Pass Solution: 
        # O(n)
        # Hangs on large test
    # init results list
    # loop through nums
    # get window slice
    # find max, add to results
    
    # results = []
    # for i in range(len(nums)):
    #     if i+k <= len(nums):
    #         window = nums[i:i+k]
    #         results.append(max(window))

    # Optimized Solution:
        # get first window
        # determine current max
        # append current max to results
        # pop first item in window
        # determine new value2
        # if popped val is current max
            # determine new current max
        # else if new value is greater than current max
            # update current max to new value
        
        # append new value to window

    results = []
    window = nums[:k]
    cur_max = max(window)
    results.append(cur_max)
    for i in range(k, len(nums)):
        pop_val = window.pop(0)
        next_val = nums[i]
        window.append(next_val)
        if pop_val == cur_max:
            cur_max = max(window)
        elif next_val > cur_max:
            cur_max = next_val
        results.append(cur_max)
    return results


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
