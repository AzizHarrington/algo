from functools import reduce

from data_structures.list.unordered import UnorderedList


class HashTable:

    def __init__(self, size=11):
        self.size = size
        self.keys = [UnorderedList() for x in range(self.size)]
        self.values = [UnorderedList() for x in range(self.size)]

    def __setitem__(self, key, val):
        position = self._hash(key)
        keys = self.keys[position]
        vals = self.values[position]
        if keys.index(key) == -1:
            # if key not found, add it
            keys.add(key)
        else:
            # else if key is present, remove old value
            value = self._get_value(key)
            vals.remove(value)
        vals.add(val)

    def __getitem__(self, key):
        return self._get_value(key)

    def __delitem__(self, key):
        pos = self._hash(key)
        value = self._get_value(key)  # do this before delete key!!!
        self.keys[pos].remove(key)
        self.values[pos].remove(value)

    def __contains__(self, key):
        pos = self._hash(key)
        return self.keys[pos].index(key) != -1

    def __len__(self):
        return reduce(lambda a, b: a + b.size(), self.keys, 0)

    def _get_key_index(self, key):
        pos = self._hash(key)
        try:
            key_pos = self.keys[pos].index(key)
        except AttributeError:
            raise KeyError("%s" % key)
        return key_pos

    def _get_value(self, key):
        pos = self._hash(key)
        key_pos = self._get_key_index(key)
        return self.values[pos].get(key_pos)

    def _hash(self, key):
        # keys must be immutable
        assert isinstance(key, (str, int, tuple, float))
        number = 0
        for index, char in enumerate(str(key)):
            number += (ord(char) * (index + 1))
        return number % self.size


def test():
    ht = HashTable()
    assert ht.__class__ == HashTable
    ht['foo'] = 'bar'
    assert ht['foo'] == 'bar'
    ht['foo'] = 'blah'
    assert ht['foo'] == 'blah'
    ht[3] = 'three'
    ht['tree'] = 'apple'
    assert 'tree' in ht
    assert len(ht) == 3
    del ht[3]
    assert len(ht) == 2

    print('hashtable tests passed')


if __name__ == "__main__":

    test()
