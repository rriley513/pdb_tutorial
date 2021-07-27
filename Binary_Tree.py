class Binary_Tree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def set_root(self, t):
        self.root = t
        return self

    def set_left(self, node):
        self.left = node
        return self

    def set_right(self, node):
        self.right = node
        return self

# let's make a tree that looks like a binary search tree, with prime numbers
def build_sample_tree():
    prime_bst = Binary_Tree().set_root(19).set_left(\
        Binary_Tree().set_root(11).set_left(\
            Binary_Tree().set_root(5).set_left(\
                Binary_Tree().set_root(3).set_left(2)).set_right(7)).set_right(\
                    Binary_Tree().set_root(13).set_right(17)))\
                    .set_right(Binary_Tree().set_root(41).set_left(23).set_right(43))

    return prime_bst
