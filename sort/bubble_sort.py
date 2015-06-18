from helpers import test_runtime


def bubble_sort(a_list):
    number_of_passes = len(a_list) - 1
    is_sorted = False
    while number_of_passes > 0 and not is_sorted:
        is_sorted = True
        for pos in range(number_of_passes):
            if a_list[pos] > a_list[pos+1]:
                is_sorted = False
                a_list[pos], a_list[pos+1] = a_list[pos+1], a_list[pos]
        number_of_passes -= 1
    return a_list


def test():
    assert bubble_sort([1, 3, 0, 4, 2]) == [0, 1, 2, 3, 4]
    assert bubble_sort([]) == []
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert test_runtime(1000, bubble_sort) < 1.0  # seconds
    print("bubble sort tests passed")


if __name__ == "__main__":

    test()
