
def int2base(integer, base):
    digits = "0123456789"
    if integer < 10:
        return digits[integer]
    return int2base((integer/base), base) + int2base((integer%base), base)


def test():
    num1 = 769

    assert int2base(num1, 10) == "769"

    print "tests passed"


if __name__ == "__main__":

    test()