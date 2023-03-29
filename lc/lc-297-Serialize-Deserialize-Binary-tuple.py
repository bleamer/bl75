#lc-297: Serialize and Deserialize Binary Tree

# Crazy solution - serializing using tuples with recursion
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solutions/396124/python-very-easy-to-understand-recursive-preorder-with-comments/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:
    NONE = '*'
    def serialize(self, root):
        if not root:
            return NONE
        # store the nodes as tuple of tuples of 
        return root.val, self.serialize(root.left), self.serialize(root.right)
    
    def deserialize(self, data):

        if data[0] == NONE:
            return None
        
        node = TreeNode(data[0])
        node.left = TreeNode(self.deserialize(data[1]))
        node.right = TreeNode(self.deserialize(data[2]))
        return node