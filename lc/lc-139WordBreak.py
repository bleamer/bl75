# lc-139 Word Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict)
        # dp[i] can s[:i] be segmented or not
        dp = [False] * (len(s) + 1)
        
        # 0 char string can exist
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                # Check if s[i:j] is in wordDict, that this new segment is in wordDict or not
                # and dp[j] we have already checked if s[:j] can be segmented or not
                if dp[j] and s[j:i] in wordSet:
                    # if so then set the dp[i] to be true
                    dp[i] = True
                    break
                # if not then keep advancing j till something found
        return dp[len(s)]


""" Complexity analysis
Outer Loop: The outer loop runs from i = 1 to len(s), iterating O(n) times, where n is the length of the string s.

Inner Loop: The inner loop runs from j = 0 to i - 1 for each i. In the worst case (when no early termination occurs), this results in O(n) iterations for each i.

Substring Check: The substring check s[j:i] in word_set is O(k), where k is the average length of a word in wordDict. However, since the dictionary is stored as a set, the membership check itself is O(1), making this step negligible.

Overall Time Complexity: The total time complexity is O(n^2), since the inner loop contributes O(n) for each of the O(n) iterations of the outer loop.

The space complexity of the given solution is as follows:

DP Array: The dp array of size n + 1 requires O(n) space.

Word Set: The word dictionary is converted to a set for fast lookups. If there are m words in wordDict, and the average word length is k, the space used by the set is O(m * k).

Substring Storage: Although the algorithm computes substrings s[j:i], they are not stored explicitly, so no extra space is used here.

Overall Space Complexity: The total space complexity is O(n + m * k), where n is the length of s, m is the number of words in wordDict, and k is the average word length.
"""