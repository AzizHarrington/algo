from insertion_sort import insertion_sort


def merge_sort(a_list):
    length = len(a_list)
    if length <= 1:
        return a_list
    split = length // 2
    right = merge_sort(a_list[:split])
    left = merge_sort(a_list[split:])
    return insertion_sort(left + right)


def test():
    assert merge_sort([0, 2, 4, 3, 1]) == [0, 1, 2, 3, 4]
    assert merge_sort([]) == []
    assert merge_sort([2, 4, 2, 4]) == [2, 2, 4, 4]
    assert merge_sort([1, 2, 3]) == [1, 2, 3]
    print("merge sort tests passed")

def test_runtime(size):
    import random
    l = list(range(size))
    random.shuffle(l)
    import time
    start = time.time()
    merge_sort(l)
    end = time.time() - start
    print("List of {} elements took {} seconds to sort".format(size, end))


if __name__ == "__main__":

    test_runtime(10000)

