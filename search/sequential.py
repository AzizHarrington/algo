def sequential_search(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]

print(sequential_search(testlist, 3))
print(sequential_search(testlist, 13))


def ordered_sequential_search(alist, item):
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]

print(ordered_sequential_search(testlist, 3))
print(ordered_sequential_search(testlist, 13))