


def linearSearch(L,T):
    indices = []

    for index in range(len(L)):
        if L[index] == T:
            indices.append(index)
    return indices