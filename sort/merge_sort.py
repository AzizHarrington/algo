from helpers import test_runtime


def merge_sort(a_list):
    length = len(a_list)
    if length <= 1:
        return a_list
    split = length // 2
    right = a_list[:split]
    left = a_list[split:]
    merge_sort(right)
    merge_sort(left)

    r = 0
    l = 0
    x = 0
    while x < length:
        if r >= len(right):
            a_list[x] = left[l]
            l += 1
        elif l >= len(left):
            a_list[x] = right[r]
            r += 1
        elif right[r] < left[l]:
            a_list[x] = right[r]
            r += 1
        else:
            a_list[x] = left[l]
            l += 1
        x += 1
    return a_list


def test():
    assert merge_sort([0, 2, 4, 3, 1]) == [0, 1, 2, 3, 4]
    assert merge_sort([]) == []
    assert merge_sort([2, 4, 2, 4]) == [2, 2, 4, 4]
    assert merge_sort([1, 2, 3]) == [1, 2, 3]
    assert test_runtime(10000, merge_sort) < 1.0  # seconds
    print("merge sort tests passed")


if __name__ == "__main__":

    test()

