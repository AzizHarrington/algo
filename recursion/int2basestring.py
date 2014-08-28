
def int2base(integer, base):
    digits = "0123456789ABCDEF"
    if integer < base:
        return digits[integer]
    return int2base((integer/base), base) + int2base((integer%base), base)


def test():
    num1 = 769
    num2 = 1453

    assert int2base(num1, 10) == "769"

    assert int2base(num2, 16) == "5AD"

    print "tests passed"


if __name__ == "__main__":

    test()