from stack import Stack


def evaluator(exp):
    """takes simple (*/+-) postfix expression and returns result"""
    s = Stack()
    tokens = exp.split()
    for t in tokens:
        if t.isdigit():
            s.push(t)
        elif t in "*/-+":
            op2 = s.pop()  # second op appears first on stack
            op1 = s.pop()  # first operand is next
            result = eval("{}{}{}".format(op1, t, op2))
            s.push(result)
    return s.pop()  # return final result from stack


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