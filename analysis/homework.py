import timeit, random


for i in [1000, 10000, 100000]:
    t = timeit.Timer("x[a_list[random.randrange(%d)]" % i,
                    "from __main__ import a_list")
    a_list = list(range(i))
    time = t.timeit(1000)
    print(i, time)