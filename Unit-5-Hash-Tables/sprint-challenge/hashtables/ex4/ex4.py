def has_negatives(a):
    """
    Accepts list of ints, returns list of positive ints that have corresponding 
        negative int.
    """
    positives = [num for num in a if num > 0]
    negatives = [num for num in a if num < 0]
    results = []

    for pos in positives:
        if -pos in negatives:
            results.append(pos)

    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
