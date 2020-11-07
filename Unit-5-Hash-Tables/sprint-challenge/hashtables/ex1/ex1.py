def get_indices_of_item_weights(weights, length, limit):
    """
    Givn package with weight 'limit' and list of item 'weights,'
        return two item index tuple whose sum of weights equals the limit.

    Higher value item goes in index 0, and smaller in index 1. If no pair exists,
        return None.
    """
    results = []

    for idx, wt in enumerate(weights):
        matching_wt = limit - wt
        if matching_wt in weights:
            results.extend([weights.index(matching_wt, idx+1), idx])
            break
        
    if results:
        results = sorted(results, reverse=True)
        return tuple(results)
    else:
        return None



