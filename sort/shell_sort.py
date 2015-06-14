from insertion_sort import insertion_sort

def shell_sort(a_list):
    gaps = get_gaps(len(a_list))
    for gap in gaps:
        for start_pos in range(gap):
            sublist = a_list[start_pos::gap]
            sorted_sublist = insertion_sort(sublist)
            a_list[start_pos::gap] = sorted_sublist
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

    test()
