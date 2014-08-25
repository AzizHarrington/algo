class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext


def test():
    n = Node(23)

    assert n.get_data() == 23
    assert n.get_next() == None

    n.set_data("tree")

    assert n.get_data() == "tree"

    print("tests pass")


if __name__ == "__main__":

    test()