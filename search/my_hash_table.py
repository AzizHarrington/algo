from data_structures.list.ordered import OrderedList


class HashTable:

    def __init__(self, size=11):
        self.size = size
        self.keys = [OrderedList() for x in range(self.size)]
        self.values = [OrderedList() for x in range(self.size)]

    def put(self, key, val):
        pos = self._hash(key)
        self.keys[pos].add(key)
        self.values[pos].add(val)

    def _hash(self, key):
        # keys must be immutable
        assert isinstance(key, (str, int, tuple, float))
        number = 0
        for index, char in enumerate(str(key)):
            number += (ord(char) * (index + 1))
        return number % self.size

    def get(self, key):
        table_pos = self._hash(key)
        list_pos = self.keys[table_pos].index(key)
        return self.values[table_pos].get(list_pos)

    def __del__(self):
        pass

    def len(self):
        pass

    def __contains__(self):
        pass


def test():
    ht = HashTable()
    assert ht.__class__ == HashTable


if __name__ == "__main__":

    test()