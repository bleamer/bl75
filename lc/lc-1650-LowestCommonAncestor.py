# lc-1650: Lowest common ancestor of binary tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Input: root = [1,2], p = 1, q = 2
# Output: 1


# Constraints:

#     The number of nodes in the tree is in the range [2, 105].
#     -10e9 <= Node.val <= 10e9
#     All Node.val are unique.
#     p != q
#     p and q will exist in the tree.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = self.right = None


class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode)-> TreeNode:
        # traverse from this node downwards and see if you find p or q
        # stop traversing if you find p or q we need not go deeper
        if not root or root == p or root == q:
            return root


        # we did not find p or q in the same subtree they must be in different
        # subtrees
        # Recursively search for p and q    
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        
        # both left and right found in different subtree
        # then this root must be LCA
        if left and right:
            return root
        
        return left if left else right


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

        data = [3,5,1,6,2,0,8,None,None,7,4]
        root = build_tree(data)
        p = root.left
        q = root.right
        lca = self.solution.lowest_common_ancestor(root, p, q)
        self.assertEqual(lca.val, 3)

    def test2(self):
        data = [3,5,1,6,2,0,8,None,None,7,4]
        root = build_tree(data)
        p = root.left
        q = root.left.right
        lca = self.solution.lowest_common_ancestor(root, p, q)
        self.assertEqual (lca.val, 5)

    def test3(self):
        data = [1,2]
        root = build_tree(data)
        p = root
        q = root.left
        lca = self.solution.lowest_common_ancestor(root, p, q)
        self.assertEqual(lca.val,  1)



if __name__ == '__main__':
    unittest.main()