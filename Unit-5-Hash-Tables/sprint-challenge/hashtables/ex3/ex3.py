def intersection(arrays):
    """
    Returns intersection between a list of lists of integers.
        ie. numbers that exist in all lists.
    """
    num_counts = {}
    combined_arrs = []
    matching_count = len(arrays)
    intersection = []

    for arr in arrays:
        combined_arrs.extend(arr)

    for num in combined_arrs:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    for num, count in num_counts.items():
        if count == matching_count:
            intersection.append(num)

    return intersection



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
