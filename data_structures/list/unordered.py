from node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        str_rpr = '['
        while current:
            str_rpr += str(current.get_data())
            if current.get_next():
                str_rpr += ', '
            current = current.get_next()
        return str_rpr + ']'

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
        current = self.head
        index = -1
        while current:
            index += 1
            if current.get_data() == item:
                return index
            current = current.get_next()
        return -1

    def append(self, item):
        new_node = Node(item)
        current = self.head
        while current:
            # at the end of the list
            if not current.get_next():
                current.set_next(new_node)
                break
            current = current.get_next()
        else:
            # empty list, so set as first item
            self.head = new_node

    def insert(self, position, item):
        new_node = Node(item)
        current = self.head
        prev = None
        current_pos = 0
        while current:
            if current_pos == position:
                if not prev:
                    # at the beginning of the list,
                    # so link new node to current head
                    new_node.set_next(current)
                    # and assign new node to list head
                    self.head = new_node
                else:
                    # insert new_node
                    new_node.set_next(current)
                    prev.set_next(new_node)
                break
            prev, current = current, current.get_next()
            current_pos += 1
        else:
            self.append(item)
                
    def pop(self, position=None):
        current = self.head
        prev = None
        current_pos = 0
        while current:
            if current_pos == position:
                if not prev:
                    # at head, so reassign to next node
                    self.head = current.get_next()
                else:
                    # break link to current
                    temp = current.get_next()
                    prev.set_next(temp)
                # finally return current
                return current.get_data()
            elif not position and not current.get_next():
                prev.set_next(None)
                return current.get_data()
            prev, current = current, current.get_next()
            current_pos += 1


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
    assert ul.index("frank") == -1

    ul.append("pizza")
    assert ul.search("pizza") == True
    assert ul.size() == 4

    ul2 = UnorderedList()

    ul2.append("hello world")
    assert ul2.size() == 1

    ul.insert(0, 4.5)
    assert ul.index(4.5) == 0
    assert ul.size() == 5

    ul.insert(2, 100)
    assert ul.index(100) == 2
    assert ul.size() == 6

    ul3 = UnorderedList()

    ul3.insert(0, 3)
    assert ul3.size() == 1

    ul3.add(2)
    ul3.add("hello")
    ul3.add(True)
    assert ul3.pop() == 3
    assert ul3.pop(0) == True
    assert ul3.size() == 2

    l = UnorderedList()

    for i in range(10):
        l.add(i)

    assert l.__str__() == '[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]'

    print("tests pass")


if __name__ == "__main__":

    test()
