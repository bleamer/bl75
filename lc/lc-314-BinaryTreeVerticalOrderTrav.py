# lc-314-Binary Tree Vertical Order Traversal


# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

# Return the vertical order traversal of the binary tree.


# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation:
# Column -1: Only node 9 is in this column.
# Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
# Column 1: Only node 20 is in this column.
# Column 2: Only node 7 is in this column.


# Input: root = [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# Column -2: Only node 4 is in this column.
# Column -1: Only node 2 is in this column.
# Column 0: Nodes 1, 5, and 6 are in this column.
#           1 is at the top, so it comes first.
#           5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
# Column 1: Only node 3 is in this column.
# Column 2: Only node 7 is in this column.



# Input: root = [1,2,3,4,6,5,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# This case is the exact same as example 2, but with nodes 5 and 6 swapped.
# Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.

 

# Constraints:

#     The number of nodes in the tree is in the range [1, 1000].
#     0 <= Node.val <= 1000




from typing import List
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = self.right = None



class Solution:
    def vertical_order_traversal(self, root: TreeNode)-> List[List[int]]:
        col_table = defaultdict(list)

        # create a queue which store BFS travesal along with 
        # coordinates in the form (node, row, column)
        queue = deque([(root, 0, 0)])

        # do BFS
        while queue:
            node, row, column = queue.popleft()
            if node:
                col_table[column].append((row, node.val))

                if node.left:
                    queue.append((node.left, row+1, column-1))
                
                if node.right:
                    queue.append((node.right, row+1, column+1))

        result = []

        # sorting over columns to maintain vertical order
        for key in sorted(col_table.keys()):
            # at a given column level sort from row lowest to highest / top to down
            nodes = [val for row, val in sorted(col_table[key])]
            result.append(nodes)
        return result





def build_tree(values) -> TreeNode:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while(i < len(values)):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

import unittest

class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test1(self):
        data = [1,2,3,4,5,6,7]
        root = build_tree(data)
        expected_out = [[4], [2], [1, 5, 6], [3], [7]]
        out = self.solution.vertical_order_traversal(root)
        self.assertListEqual(expected_out, out)

    def test2(self):
        data = [3, 9, 20, None, None, 15, 7]
        root = build_tree(data)
        expected_out = [[9], [3, 15], [20], [7]]
        out = self.solution.vertical_order_traversal(root)
        self.assertListEqual(expected_out, out)

    def test3(self):
        data = [1, 2, 3, 4, 6, 5, 7]
        root = build_tree(data)
        expected_out = [[4], [2], [1, 5, 6], [3], [7]]
        out = self.solution.vertical_order_traversal(root)
        self.assertListEqual(expected_out, out)


if __name__ == '__main__':
    unittest.main()