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

        def dfsmaxsum(node, maxsum):
            if node is None:
                return 0
            # if node.right is None and node.left is None:
            #     return node.val
            l = dfsmaxsum(node.left, maxsum)
            r = dfsmaxsum(node.right, maxsum)
            nodemaxsum = l + r + node.val
            if nodemaxsum > maxsum:
                maxsum = nodemaxsum

            return maxsum
        maxsum = -sys.maxsize
        return dfsmaxsum(root, maxsum)