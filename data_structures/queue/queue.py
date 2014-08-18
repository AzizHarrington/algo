class Queue:
    def __init__(self):
        self.items = list()

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def test():
    q = Queue()

    assert q.is_empty()

    q.enqueue(4)
    q.enqueue("dog")
    q.enqueue(True)

    assert q.size() == 3
    assert q.is_empty() == False

    q.enqueue(8.4)

    assert q.dequeue() == 4
    assert q.dequeue() == "dog"
    assert q.size() == 2

    print("tests pass")


if __name__ == "__main__":

    test()