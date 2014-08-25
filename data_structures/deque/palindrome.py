from deque import Deque 


def checker(astring):
    d = Deque()

    for a in astring:
        d.add_front(a)

    while True:
        if d.is_empty() or d.size() == 1:
            return True
        if d.remove_front() == d.remove_rear():
            continue
        else:
            return False


def test():

    assert checker("bob") == True
    assert checker("") == True
    assert checker("b") == True
    assert checker("racecar") == True
    assert checker("bbbbbbbb") == True

    assert checker("hamburger") == False
    assert checker("tim") == False

    print("tests pass")


if __name__ == "__main__":

    test()