from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.

    def helper(tree):
        if not tree:
            return True;
            if tree.data < tree.left.data or tree.data > tree.right.data:
                return False
            else:
                helper(tree.left)
                helper(tree.right)
        return True

    return helper(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
