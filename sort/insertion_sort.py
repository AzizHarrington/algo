def insertion_sort(a_list):
    for index, item in enumerate(a_list):
        for x, comparison in enumerate(a_list[index::-1]):
            comparison_index = index - x
            if item < comparison:
                if item >= a_list[comparison_index - 1] or comparison_index == 0:
                    a_list.pop(index)
                    a_list.insert(comparison_index, item)
    return a_list


def test():
    assert insertion_sort([0, 2, 4, 3, 1]) == [0, 1, 2, 3, 4]
    assert insertion_sort([]) == []
    assert insertion_sort([2, 4, 2, 4]) == [2, 2, 4, 4]
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]
    print("insertion sort tests passed")


if __name__ == "__main__":

    test()
