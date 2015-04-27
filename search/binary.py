def binary_search(alist, item):
    found = False

    while not found and len(alist) > 0:
        mid_point = len(alist) // 2
        if alist[mid_point] == item:
            found = True
        elif alist[mid_point] < item:
            alist = alist[mid_point + 1:]
        else:
            alist = alist[:mid_point]

    return found


def recursive_binary_search(alist, item):
    if not alist:
        return False
    mid_point = len(alist) // 2
    if alist[mid_point] == item:
        return True
    elif alist[mid_point] > item:
        return recursive_binary_search(alist[:mid_point], item)
    elif alist[mid_point] < item:
        return recursive_binary_search(alist[mid_point+1:], item)


test_list = [1, 2, 6, 9, 10, 11, 17, 40, 45]


def test():
    assert binary_search(test_list, 17)
    assert binary_search(test_list, 6)
    assert binary_search(test_list, 1)
    assert binary_search(test_list, 45)
    assert not binary_search(test_list, 15)

    assert recursive_binary_search(test_list, 17)
    assert recursive_binary_search(test_list, 6)
    assert recursive_binary_search(test_list, 1)
    assert recursive_binary_search(test_list, 45)
    assert not recursive_binary_search(test_list, 15)

    print("binary search tests pass")


if __name__ == "__main__":
    test()
