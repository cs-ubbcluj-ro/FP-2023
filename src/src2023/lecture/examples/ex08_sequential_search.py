def search_iter(data: list, key):
    for i in range(len(data)):
        if data[i] == key:
            return i
    return -1


def search_rec(data: list, key, pos: int = 0):
    if 0 > pos or pos >= len(data):
        return -1
    if data[pos] == key:
        return key
    return search_rec(key, data, pos + 1)
