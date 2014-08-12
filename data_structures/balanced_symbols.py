from stack import Stack


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


if __name__ == '__main__':

    test_sym_checker()