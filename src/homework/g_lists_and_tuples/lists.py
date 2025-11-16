def get_p_distance(list1, list2):
    # count positions where symbols differ
    diffs = 0
    for a, b in zip(list1, list2):
        if a != b:
            diffs += 1
    return diffs / len(list1)


def get_p_distance_matrix(list_of_lists):
    n = len(list_of_lists)
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            # distance from list i to list j
            if i == j:
                row.append(0.0)
            else:
                row.append(round(get_p_distance(list_of_lists[i], list_of_lists[j]), 5))
        matrix.append(row)

    return matrix
