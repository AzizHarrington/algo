from stack import Stack


def converter(exp, fix="post"):
    """takes simple infix expression and converts to prefix or postfix"""
    tokens = list(exp)
    open_paren, close_paren = "(", ")"

    if fix not in ["pre", "post"]:
        raise ValueError("Must specify fix as either 'pre' or 'post'")

    if fix == "pre":
        tokens.reverse()
        open_paren, close_paren = ")", "("

    s = Stack()
    result = ''

    for t in tokens:
        if t == open_paren:
            pass
        elif t in ["*", "+", "-", "/"]:
            s.push(t)
        elif t == close_paren and not s.is_empty():
            result += s.pop()
        else:
            result += t

    if fix == "pre":
        return result[::-1]
    return result


def test():
    in_exp1 = "((A+B)*C)"
    pre_exp1 = "*+ABC"
    post_exp1 = "AB+C*"

    assert converter(in_exp1, "pre") == pre_exp1
    assert converter(in_exp1, "post") == post_exp1

    print("tests pass")


if __name__ == "__main__":

    test()