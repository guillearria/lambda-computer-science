'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import time

def sliding_window_max(nums, k):
    start = time.perf_counter()
    # init results list
    # loop through nums
    # get window slice
    # find max, add to results
    results = []
    for i in range(len(nums)):
        if i+k <= len(nums):
            window = nums[i:i+k]
            results.append(max(window))
    
    end = time.perf_counter()
    print("Runtime:", end-start, "seconds")
    return results


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
