from node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        while current:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        current = self.head
        prev = None
        while current:
            if current.get_data() == item:
                if not prev:
                    self.head = current.get_next()
                else:
                    prev.set_next(current.get_next())
                break
            prev, current = current, current.get_next()

    def index(self, item):
        pass

    def append(self, item):
        pass

    def insert(self, position, item):
        pass

    def pop(self, position=0):
        pass


def test():
    ul = UnorderedList()

    assert ul.size() == 0
    ul.add(2)
    ul.add(1)
    assert ul.size() == 2

    ul.add("bob")
    ul.add("tree")
    assert ul.search("tree") == True
    assert ul.search("dog") == False 

    ul.remove(1)
    assert ul.search(1) == False
    assert ul.size() == 3

    assert ul.index("bob") == 1
    assert ul.index(2) == 2

    ul.append("pizza")
    assert ul.search("pizza")
    assert ul.size() == 4

    ul.insert(0, 4.5)
    assert ul.index(4.5) == 0
    assert ul.size() == 5

    assert ul.pop() == 2
    assert ul.pop(0) == 4.5
    assert ul.size() == 3

    print("tests pass")


if __name__ == "__main__":

    test()
