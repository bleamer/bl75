# 131. Palindrome Partitioning



class Solution:
    def is_palindrome(self, s: str):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        if not s: return [[]]
        result = []
        for i in range(1, len(s)+1):
            if self.is_palindrome(s[:i]):
                for suffix in self.partition(s[i:]):
                    result.append([s[:i]] + suffix)
                    print(result)
        return result



        