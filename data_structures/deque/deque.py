class Deque:
    def __init__(self):
        self.items = []

    def add_rear(self, item):
        self.items.insert(0, item)

    def add_front(self, item):
        self.items.append(item)

    def remove_rear(self):
        return self.items.pop(0)

    def remove_front(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def test():
    d = Deque()

    assert d.is_empty() == True

    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)

    assert d.size() == 4
    assert d.is_empty() == False

    d.add_rear(8.4)

    assert d.remove_rear() == 8.4
    assert d.remove_front() == True

    print("tests pass")


if __name__ == '__main__':

    test()