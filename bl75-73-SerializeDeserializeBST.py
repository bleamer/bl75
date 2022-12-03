# Definition for a binary tree node.
import collections
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    JOIN_TOKEN = ' '
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        values = []
        def preOrder(node: Optional[TreeNode], nodeList: list[TreeNode]):
            if node:
                nodeList.append(collections.deque(n for n in node))
                node.left = preOrder(node, nodeList)
                node.right = preOrder(node, nodeList)

        preOrder(root, values)
        print(JOIN_TOKEN.join(values))
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        values = collections.deque(data.split(JOIN_TOKEN))

        root = None
        def buildBSTfromList(nodeList:list[TreeNode], root: Optional[TreeNode]):
            if nodeList:
                    root = TreeNode(nodeList.pop())
                    buildBSTfromList(nodeList, root.left)
                    buildBSTfromList(nodeList, root.left)
                    return root
        return buildBSTfromList(values, root)
            


root = [2,1,3]

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()

tree = ser.serialize(root)
ans = deser.deserialize(tree)
print(ans)