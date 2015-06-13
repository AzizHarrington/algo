def shell_sort(a_list):
    gaps = get_gaps(len(a_list))
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
    print("shell sort tests passed")


if __name__ == "__main__":

    # test()
    print(get_gaps(111))
