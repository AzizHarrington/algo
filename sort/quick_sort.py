from .helpers import test_runtime


def quick_sort(a_list):
    length = len(a_list)
    if length <= 1:
        return a_list
    pivot = 0
    left = 1
    right = length - 1
    while True:
        while a_list[left] < a_list[pivot]:
            if left < length - 1:
                left += 1
            else:
                break
        while a_list[right] > a_list[pivot]:
            if right > 0:
                right -= 1
            else:
                break
        if a_list[right] <= a_list[pivot] <= a_list[left] and left >= right:
            break
        if a_list[right] == a_list[left]:
            break
        a_list[left], a_list[right] = a_list[right], a_list[left]
    a_list[right], a_list[pivot] = a_list[pivot], a_list[right]
    pivot = right
    return quick_sort(a_list[:pivot]) + [a_list[pivot]] + quick_sort(a_list[pivot + 1:])


def test():
    assert quick_sort([0, 2, 4, 3, 1]) == [0, 1, 2, 3, 4]
    assert quick_sort([]) == []
    assert quick_sort([2, 4, 2, 4]) == [2, 2, 4, 4]
    assert quick_sort([1, 2, 3]) == [1, 2, 3]
    assert test_runtime(10000, quick_sort) < 1.0  # seconds
    print("quick sort tests passed")


if __name__ == "__main__":

    test()

