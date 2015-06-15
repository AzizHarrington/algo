from insertion_sort import insertion_sort
from helpers import test_runtime


def shell_sort(a_list):
    for gap in get_gaps(len(a_list)):
        for start_pos in range(gap):
            a_list[start_pos::gap] = insertion_sort(a_list[start_pos::gap])
    return a_list


def get_gaps(size):
    gaps = []
    while size > 1:
        size //= 2
        gaps.append(size)
    return gaps


def test():
    assert shell_sort([0, 2, 4, 3, 1]) == [0, 1, 2, 3, 4]
    assert shell_sort([]) == []
    assert shell_sort([2, 4, 2, 4]) == [2, 2, 4, 4]
    assert shell_sort([1, 2, 3]) == [1, 2, 3]
    assert test_runtime(10000, shell_sort) < 1.0  # seconds
    print("shell sort tests passed")


if __name__ == "__main__":

    test()
