import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    it0, it1 = node0, node1
    visited_nodes = set()
    while it0 or it1:
        # ascend both nodes in tandem and store visited nodes in a hashmap
        if it0:
            if it0 in visited_nodes:
                return it0
            else:
                visited_nodes.add(it0)
                it0 = it0.parent
        if it1:
            if it1 in visited_nodes:
                return it1
            else:
                visited_nodes.add(it1)
                it1 = it1.parent

    raise ValueError("node 0 and node 1 are not in the same tree")


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
        generic_test.generic_test_main(
            'lowest_common_ancestor_close_ancestor.py',
            'lowest_common_ancestor.tsv', lca_wrapper))
