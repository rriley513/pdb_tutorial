import Binary_Tree

GLOBAL_VARIABLE = "You found a global variable!"

# returns a list representing a preorder traversal of the nodes of the tree
def preorder_traversal_list(binary_tree):

    traversal = []
    if binary_tree.root is not None:
        traversal.append(binary_tree.root)

    if binary_tree.left is not None:
        if isinstance(binary_tree.left, Binary_Tree.Binary_Tree):
            traversal.extend(preorder_traversal_list(binary_tree.left))
        else:
            traversal.append(binary_tree.left)

    if binary_tree.right is not None:
        if isinstance(binary_tree.right, Binary_Tree.Binary_Tree):
            traversal.extend(preorder_traversal_list(binary_tree.right))
        else:
            traversal.append(binary_tree.right)

    return traversal

if __name__ == "__main__":
    my_tree = Binary_Tree.build_sample_tree()
    print(preorder_traversal_list(my_tree))
