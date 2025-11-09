def get_lowest_list_value(values):
    """Return the lowest value in a list without using min()."""
    if not values:
        return None

    lowest = values[0]
    for v in values:
        if v < lowest:
            lowest = v
    return lowest


def get_highest_list_value(values):
    """Return the highest value in a list without using max()."""
    if not values:
        return None

    highest = values[0]
    for v in values:
        if v > highest:
            highest = v
    return highest
