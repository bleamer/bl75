# 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
         # Palindrome starts at current index
        # given current index find the longest palindrome for current 
        l = len(s)
        if len(s) < 2:
            return s

        # need to keep track of longest palindrome at current index
        def is_pld(t:str):
            tl = len(t)
            for i in range(0, tl//2):
                if t[i] != t[tl-i-1]:
                    return False
            return True

        longest_palindrome = s[0]
        def expand_from_index(left:int, right:int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        for i in range(len(s)):
            palindrome_odd = expand_from_index(i, i)
            if len(palindrome_odd) > len(longest_palindrome):
                longest_palindrome = palindrome_odd
            palindrome_even = expand_from_index(i, i+1)
            if len(palindrome_even) > len(longest_palindrome):
                longest_palindrome = palindrome_even
        return longest_palindrome
        





















