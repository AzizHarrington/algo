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


def par_checker(symbol_str):
    """takes string with parenthesis and returns true if balanced"""
    s = Stack()
    for sym in symbol_str:
        if sym == '(':
            s.push(sym)
        elif sym == ')':
            try:
                s.pop()
            except:
                return False
    return s.size() == 0


def test_par_checker():
    str1 = "((1 + 2) * (3 / 4) / (2 ** 2) + ( 1 + 1))"
    str2 = "(((((((True) or  False)"

    assert par_checker(str1) == True
    assert par_checker(str2) == False

    print("par_checker tests pass")


test_par_checker()
