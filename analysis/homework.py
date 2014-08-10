import timeit, random


# test that list index operator is Order of 1 operation
def test_list_index():
    for i in [1000, 10000, 100000, 1000000]:
        t = timeit.Timer("a_list[random.randrange(%d)]" % i,
                        "from __main__ import a_list, random")
        a_list = list(range(i))
        time = t.timeit(1000)
        print("list index", i, time)


# test get/set are O(1) for dicts
def test_get_set_dicts():
    for i in [1000, 10000, 100000, 1000000]:
        t = timeit.Timer("a_dict[random.randrange(%d)]" % i,
                        "from __main__ import a_dict, random")
        a_dict = {x:None for x in range(i)}
        get_time = t.timeit(1000)
        t = timeit.Timer("a_dict[random.randrange(%d)]=random.randrange(10)" % i,
                        "from __main__ import a_dict, random")
        a_dict = {x:None for x in range(i)}
        set_time = t.timeit(1000)
        print("dict get/set", i, get_time, set_time)


# compare del performance for lists/dicts
def test_del():
    for i in [1000, 10000, 100000, 1000000]:
        t = timeit.Timer("del(a[random.randrange(len(a))])",
                        "from __main__ import a, random")
        a = list(range(i))
        list_time = t.timeit(1000)

        t = timeit.Timer("del(a[a.keys()[0]])",
                        "from __main__ import a, random")
        a = {x:None for x in range(i)}
        dict_time = t.timeit(1000)
        print("dict vs list, del", i, list_time, dict_time)


# find kth smallest number in random list of numbers in linear time
def find_smallest(num_list):
    smallest = None
    for n in num_list:
        if not smallest or n < smallest:
            smallest = n
    return smallest


def test():
    test_list = [34, 52, 123, 20, 14, 10, 10, 12, 5, 7, 100, 9]

    assert find_smallest(test_list) == 5

    print("tests passed")


test()