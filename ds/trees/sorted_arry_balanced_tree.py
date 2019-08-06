"""CCI:
Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
write an algo­rithm to create a binary search tree with minimal height.

[1, 3, 5, 6, 9, 11, 17, 23, 53]
             9
    3               17
1      5        11      23

          6                 53

Note:
One interesting point to note here, this approach can be used for crateing a balanced BST.
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


def balanced_tree(sorted_arr, start, end) -> Node:
    # Check for empty arr
    if end < start:
        return
    # NOTE: // -> for python 3
    mid = (end + start) // 2
    node = Node(sorted_arr[mid])
    node.left = balanced_tree(sorted_arr, start, mid - 1)
    node.right = balanced_tree(sorted_arr, mid + 1, end)
    return node


if __name__ == '__main__':
    arr = [1, 3, 5, 6, 9, 11, 17, 23, 53]
    tree = balanced_tree(arr, 0, len(arr)-1)
    assert tree.key == 9
    assert tree.left.key == 3
    assert tree.right.key == 17
    assert tree.left.left.key == 1
