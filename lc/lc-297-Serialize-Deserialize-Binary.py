#lc-297: Serialize and Deserialize Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        DILIM = '|'
        NONE = 'None'
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if not node:	
                res.append(NONE)
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return DILIM.join(res)	
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        DILIM = '|'
        NONE = 'None'
        if not data:
            return None
		
        values = data.split(DILIM)
        root = TreeNode(int(values[0]))

        queue = deque()
        queue.append(root)

        i = 1
        while queue:
            node = queue.popleft()
            if values[i] != NONE:
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)

            if values[i+1] != NONE:
                node.right = TreeNode(int(values[i+1]))
                queue.append(node.right)
	

            i += 2
        return root        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))