class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
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

    assert s.is_empty() == True
    s.push(4)
    s.push('dog')
    assert s.peek() == 'dog'
    s.push(True)
    assert s.size() == 3
    assert s.is_empty() == False
    s.push(8.4)
    assert s.pop() == 8.4
    assert s.pop() == True
    assert s.size() == 2

    print("stack tests pass")


test()


def revstring(a_str):
    s = Stack()
    for a in a_str:
        s.push(a)
    revstr = ''
    while not s.is_empty():
        revstr += s.pop()
    return revstr


def sym_checker(symbol_str):
    """takes string with returns true if symbols balanced"""
    syms = {'(': ')', '[': ']', '{': '}'}
    s = Stack()
    for sym in symbol_str:
        if sym in syms.keys():
            s.push(sym)
        elif sym in syms.values():
            if syms[s.peek()] == sym:
                if not s.is_empty():
                    s.pop()
                else:
                    return False
            else:
                False
    return s.size() == 0


def test_sym_checker():
    str1 = "((1 + 2) * (3 / 4) / (2 ** 2) + ( 1 + 1))"
    str2 = "(((((((True) or  False)"
    str3 = "{ { ( [ ] [ ] ) } ( ) }"
    str4 = "( [ ) ]"

    assert sym_checker(str1) == True
    assert sym_checker(str2) == False
    assert sym_checker(str3) == True
    assert sym_checker(str4) == False

    print("sym_checker tests pass")


test_sym_checker()
