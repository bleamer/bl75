#lc-297: Serialize and Deserialize Binary Tree

# Crazy solution - serializing using tuples with recursion
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solutions/74259/recursive-preorder-python-and-c-o-n/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    NONE = "*"
    DELIM = '-'

    def serialize(self, root):
        vals = []
        def traverse(node):
            if node:
                vals.append(str(node.data))
                traverse(node.left)
                traverse(node.right)
            else:
                vals.append(NONE)

        traverse(root)
        return DELIM.join(vals)
    

    def deseralize(self, data):
        def unravel():
            val = next(vals)
            if val == NONE:
                return None
            node = TreeNode(val)
            node.left = unravel()
            node.right = unravel()
            return node
        vals = iter(data.split(DELIM))
        return unravel(data)
    

    