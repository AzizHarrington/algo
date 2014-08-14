from stack import Stack


def evaluator(exp):
    """takes postfix expression and returns result"""
    pass


def test():
    exp1 = "4 5 6 * +"
    exp2 = "7 8 + 3 2 + /"
    exp3 = "10 5 -"

    assert evaluator(exp1) == 34
    assert evaluator(exp2) == 3
    assert evaluator(exp3) == 5

    print("tests pass")


if __name__ == "__main__":

    test()