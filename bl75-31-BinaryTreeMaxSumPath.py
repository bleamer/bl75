# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
import sys
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = [root.val]
        def dfsmaxsum(node):
            if node is None:
                return 0
            # if node.right is None and node.left is None:
            #     return node.val
            l = dfsmaxsum(node.left)
            r = dfsmaxsum(node.right)
            l = max(l, 0)
            r = max(r, 0)
            maxsum[0] = max(maxsum[0], l + r + node.val)
            return node.val + max(l, r)
        dfsmaxsum(root)
        return maxsum[0]