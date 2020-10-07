'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # init results arr
    # enumarate through arr, get index
        # get left slice
        # get right slice
        # merge the two slices
        # join with multiplication sign, and eval
        # add to results

    # Attempt 1
    # results = []
    # for i, num in enumerate(arr):
    #     left_slice = arr[:i]
    #     right_slice = arr[i+1:]
    #     complete_slice = left_slice + right_slice
    #     result = eval("*".join(map(str, complete_slice)))
    #     results.append(result)
    # return results

    # Attempt 2
    results = []
    for num in arr:
        sliced = arr.copy()
        sliced.remove(num)
        result = eval("*".join(map(str, sliced)))
        results.append(result)
    return results

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
