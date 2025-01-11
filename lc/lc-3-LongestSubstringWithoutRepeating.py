# 3-Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rep = {}
        start = end = 0
        maxlen = 0
        idx = None
        for end, c in enumerate(s):
            if c in rep and rep[c] >= start:
                start = rep[c] + 1
            rep[c] = end
            maxlen =  max(maxlen, end - start+1)
        return maxlen