from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import deque


# compute the in order traversal of nodes for each depth
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    ans = []
    # init two queues: one for depth i and another one for (i + 1)
    q1: deque[BinaryTreeNode] = deque()
    q2: deque[BinaryTreeNode] = deque()

    # push the root node into 1st queue
    q1.append(tree)
    pop_q1 = 1  # if 1 pop 1st queue else 0 pop 2nd queue
    begin_depth = 1  # beginning of the traverse at a certain depth

    while q1 or q2:
        curr_depth_q, next_depth_q = (q1, q2) if pop_q1 else (q2, q1)

        # before we start traverse all the nodes in this depth from left to right (FIFO)
        # we append the queue as a list in the answer
        if begin_depth:
            ans.append([n.data for n in curr_depth_q])
            begin_depth = 0

        # push the front node's children to either 1st or 2nd queue in order
        node = curr_depth_q.popleft()
        if node.left:
            next_depth_q.append(node.left)
        if node.right:
            next_depth_q.append(node.right)
        if len(curr_depth_q) == 0:
            begin_depth = 1
            pop_q1 ^= 1  # XOR toggle pop_q1

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
