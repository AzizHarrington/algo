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
            prev = current
            current = current.get_next()
                


ul = UnorderedList()

ul.add("bob")
ul.add("tree")
ul.add(2)
ul.add(1)

print(ul.size())

ul.remove(1)

print(ul.size())
print(ul.search(1))

