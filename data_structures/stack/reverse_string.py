from stack import Stack

def revstring(a_str):
    s = Stack()
    for a in a_str:
        s.push(a)
    revstr = ''
    while not s.is_empty():
        revstr += s.pop()
    return revstr


def test():
    str1 = "hello"
    str2 = "olleh"

    assert revstring(str1) == str2

    print("tests pass")


if __name__ == "__main__":

    test()