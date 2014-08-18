from stack import Stack


def convert_dec(integer, base):
    """takes integer and returns new base number"""
    digits = '0123456789ABCDEFGHIJKLMNOP'
    s = Stack()
    while integer:
        s.push(digits[integer%base])
        integer //= base
    b = ''
    while not s.is_empty():
        b += str(s.pop())
    return b


def test_conver_dec():
    int1 = 233

    assert convert_dec(233, 2) == '11101001'
    assert convert_dec(233, 8) == '351'
    assert convert_dec(233, 16) == 'E9'

    print("dec_to_bin tests pass")


if __name__ == '__main__':
    test_conver_dec()