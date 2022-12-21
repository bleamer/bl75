# Leetcode 212

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

#  

# Example 1:

# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

# Example 2:

# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []

#  

# Constraints:

#     m == board.length
#     n == board[i].length
#     1 <= m, n <= 12
#     board[i][j] is a lowercase English letter.
#     1 <= words.length <= 3 * 104


from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.isWordinDict = False
        self.children = {}

    def addWord(self, word):
        curchar = self
        for char in word:
            if char not in curchar.children:
                curchar.children[char] = TrieNode()
            curchar = curchar.children[char]
        curchar.isWordinDict = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        visited, found = set(), set()

        def dfs(row, col, node, word):
            # boundary condition
            if (row < 0 or row >=ROWS or col < 0 or col >= COLS or\
                board[row][col] not in node.children or (row, col) in visited):
                return

            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.isWordinDict:
                found.add(word)

            dfs(row+1, col, node, word)
            dfs(row-1, col, node, word)
            dfs(row, col+1, node, word)
            dfs(row, col-1, node, word)

            visited.remove((row, col))
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")

        return list(found)




if __name__ == '__main__':
    # print([[0 for x in range(2)] for y in range(3)])
    solution = Solution()
    print(solution.findWords([["a","a"]], ["a"]))
    print(solution.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))