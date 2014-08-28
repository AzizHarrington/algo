from node import Node 
from unordered import UnorderedList

class OrderedList(UnorderedList):
    def __init__(self):
        UnorderedList.__init__(self)

    def add(self, item):
        temp = Node(item)
        current = self.head
        prev = None
        while current:
            # if node with greater value is found,
            # insert item
            if temp.get_data() < current.get_data():
                if not prev:
                    self.head = temp
                else:
                    prev.set_next(temp)
                temp.set_next(current)
                return
            # reached the end of the list without finding
            # a greater value node
            elif not current.get_next():
                current.set_next(temp)
                return
            prev, current = current, current.get_next()
        # if no assignments, list empty, set head
        self.head = temp

    def search(self, item):
        current = self.head
        while current:
            if current.get_data() == item:
                return True
            if current.get_data() > item:
                break
            current = current.get_next()
        return False

    def insert(self, *args, **kwargs):
        raise AttributeError("OrderedList has no attribute 'insert'")


def test():

    o = OrderedList()

    assert o.is_empty()
    o.add(1)
    o.add(2)
    o.add(5)
    o.add(3)
    o.add(4)
    assert o.size() == 5
    o.remove(1)
    assert o.size() == 4
    assert o.search(2) == True
    assert o.search(5) == True
    assert o.search(1) == False

    two = OrderedList()

    assert two.search(3) == False
    two.add(1)
    assert two.search(1) == True

    print("tests pass")


if __name__ == "__main__":

    test()
