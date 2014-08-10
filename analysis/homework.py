import timeit, random


# test that list index operator is Order of 1 operation
for i in [1000, 10000, 100000, 1000000]:
    t = timeit.Timer("a_list[random.randrange(%d)]" % i,
                    "from __main__ import a_list, random")
    a_list = list(range(i))
    time = t.timeit(1000)
    print("list index", i, time)


# test get/set are O(1) for dicts
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