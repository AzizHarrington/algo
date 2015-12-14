import operator

from binary_tree import BinaryTree
from data_structures.stack.stack import Stack


def build_parse_tree(expression):
    tokens = expression.split()
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    current_tree = tree
    for token in tokens:
        if token == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif token not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(int(token))
            parent = stack.pop()
            current_tree = parent
        elif token in ['+', '-', '*', '/']:
            current_tree.set_root_val(token)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif token == ')':
            current_tree = stack.pop()
        else:
            raise ValueError
    return tree


def evaluate(parse_tree):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()

    if left_child and right_child:
        func = operators[parse_tree.get_root_val()]
        return func(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.get_root_val()
