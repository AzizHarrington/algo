

def reverse(a_string):
    if len(a_string) <= 1:
        return a_string
    return reverse(a_string[1:]) + reverse(a_string[0])


def test():

    str1 = "pizza"
    str2 = "test"

    assert reverse(str1) == str1[::-1]
    assert reverse(str2) == str2[::-1]

    print("tests pass")


if __name__ == "__main__":

    test()