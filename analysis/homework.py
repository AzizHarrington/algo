import timeit, random


# test that list index operator is Order of 1 operation
for i in [1000, 10000, 100000, 1000000]:
    t = timeit.Timer("a_list[random.randrange(%d)]" % i,
                    "from __main__ import a_list, random")
    a_list = list(range(i))
    time = t.timeit(1000)
    print("list size", i, time)


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
    print("dict size", i, get_time, set_time)