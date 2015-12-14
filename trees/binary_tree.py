class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


def test():
    tree = BinaryTree('a')
    assert tree.get_root_val() == 'a'
    assert tree.get_left_child() is None
    tree.insert_left('b')
    assert isinstance(tree.get_left_child(), BinaryTree)
    assert tree.get_left_child().get_root_val() == 'b'
    tree.insert_right('c')
    assert isinstance(tree.get_right_child(), BinaryTree)
    assert tree.get_right_child().get_root_val() == 'c'
    tree.get_right_child().set_root_val('hello')
    assert tree.get_right_child().get_root_val() == 'hello'
    tree.insert_left('d')
    assert tree.get_left_child().get_root_val() == 'd'
    assert tree.get_left_child().get_left_child().get_root_val() == 'b'

    print('tests passed')

def test_print():
    pass


if __name__ == '__main__':
    test()
