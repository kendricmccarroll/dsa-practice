from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    # TODO - you fill in here.


    def helper(node, parent=0):
        if not node:
            return 0

        parent=parent*2 + node.data
        if node.left == None and node.right==None:
            return parent
        return(helper(node.left, parent) + helper(node.right, parent))


    return helper(tree, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
