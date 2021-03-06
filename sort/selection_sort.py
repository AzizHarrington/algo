import sys
from collections import namedtuple

from .helpers import test_runtime


sys.setrecursionlimit(10000)


# not really selection sort, since it uses two lists....
# TODO: refactor to only use one list....
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
    assert recursive_selection_sort([2, 0, 1, 3, 4]) == [0, 1, 2, 3, 4]
    assert recursive_selection_sort([]) == []
    assert recursive_selection_sort([1, 2, 3]) == [1, 2, 3]
    assert test_runtime(1000, recursive_selection_sort) < 1.0  # seconds
    print("selection sort tests passed")


if __name__ == "__main__":

    test()
