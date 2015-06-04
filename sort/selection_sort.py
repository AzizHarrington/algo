import random
from collections import namedtuple


def _random_list(n):
    random_list = range(n)
    random.shuffle(random_list)
    return random_list


def recursive_selection_sort(unsorted_list, sorted_list=None):
    if not unsorted_list:
        return sorted_list or []
    if not sorted_list:
        sorted_list = []
    largest = namedtuple('Largest', ['value', 'position'])
    largest.value = None
    for position, value in enumerate(unsorted_list):
        if largest.value is None or value > largest.value:
            largest.position, largest.value = position, value
    unsorted_list.pop(largest.position)
    sorted_list.insert(0, largest.value)
    return recursive_selection_sort(unsorted_list, sorted_list)


def test():
    assert recursive_selection_sort(_random_list(5)) == [0, 1, 2, 3, 4]
    assert recursive_selection_sort([]) == []
    assert recursive_selection_sort([1, 2, 3]) == [1, 2, 3]
    print("selection sort tests passed")


if __name__ == "__main__":

    test()
