def insertion_sort(a_list):
    for index, item in enumerate(a_list):
        for comparison in a_list[index::-1]:
            print(index, item, comparison)


def test():
    assert insertion_sort([0, 2, 4, 3, 1]) == [0, 1, 2, 3, 4]
    assert insertion_sort([]) == []
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]
    print("insertion sort tests passed")


if __name__ == "__main__":

    # test()
    insertion_sort([1,2,3,4,5])