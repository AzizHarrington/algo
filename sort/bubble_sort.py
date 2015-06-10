import random


def recursive_bubble_sort(a_list, is_sorted=False):
    if is_sorted:
        return a_list

    is_sorted = True
    for pos, item in enumerate(a_list):
        if pos + 1 == len(a_list):
            break
        other = a_list[pos+1]
        if item > other:
            is_sorted = False
            a_list[pos], a_list[pos+1] = other, item

    return recursive_bubble_sort(a_list, is_sorted)


def test():
    random_list = list(range(5))
    random.shuffle(random_list)
    assert recursive_bubble_sort(random_list) == [0, 1, 2, 3, 4]
    assert recursive_bubble_sort([]) == []
    assert recursive_bubble_sort([1, 2, 3]) == [1, 2, 3]
    print("bubble sort tests passed")


if __name__ == "__main__":

    test()
