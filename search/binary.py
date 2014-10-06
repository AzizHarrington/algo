def binary_search(alist, item):
    found = False

    while not found and len(alist) > 0:
        mid_point = len(alist) / 2
        if alist[mid_point] == item:
            found = True
        elif alist[mid_point] < item:
            alist = alist[mid_point + 1:]
        else:
            alist = alist[:mid_point]

    return found


test_list = [1, 2, 6, 9, 10, 11, 17, 40, 45]

print(binary_search(test_list, 17))
print(binary_search(test_list, 6))
print(binary_search(test_list, 1))
print(binary_search(test_list, 45))
print(binary_search(test_list, 15))