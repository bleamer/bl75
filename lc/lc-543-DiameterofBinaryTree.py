# lc-543-DiameterofBinaryTree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        global maxdia
        maxdia = 0
        def depth(p):
            global maxdia
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            maxdia = max(maxdia, left+right)
            return 1 + max(left, right)
            
        depth(root)
        return maxdia
        