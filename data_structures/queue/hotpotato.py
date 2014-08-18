from queue import Queue


def hotpotato(names, num):
    q = Queue()
    for name in names:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(1, num+1):
            if i == num:
                q.dequeue()
            else:
                q.enqueue(q.dequeue())

    return q.dequeue()


print(hotpotato(["bob", "john", "kate", "sara"], 3))