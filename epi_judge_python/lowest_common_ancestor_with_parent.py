import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def find_depth(node: BinaryTreeNode):
        depth = 0
        while node.parent:
            node = node.parent
            depth += 1
        return depth

    node0_depth, node1_depth = map(find_depth, (node0, node1))

    # always make node 0 the deeper one
    if node1_depth > node0_depth:
        node0, node1 = node1, node0

    # ascends from the deeper node
    for _ in range(abs(node0_depth - node1_depth)):
        node0 = node0.parent

    # now node 0 & 1 at same depth, move them in tandem until we reach the LCA
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent

    return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
