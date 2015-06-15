import random


def test_runtime(size, sortfunc):
    import random
    l = list(range(size))
    random.shuffle(l)
    import time
    start = time.time()
    sortfunc(l)
    end = time.time() - start
    return end
