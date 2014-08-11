class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def test():
    s = Stack()

    assert s.isEmpty() == True
    s.push(4)
    s.push('dog')
    assert s.peek() == 'dog'
    s.push(True)
    assert s.size() == 3
    assert s.isEmpty() == False
    s.push(8.4)
    assert s.pop() == 8.4
    assert s.pop() == True
    assert s.size() == 2

    print("tests pass")


test()