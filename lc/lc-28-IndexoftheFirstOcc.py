# LC 28. Find the Index of the First Occurrence in a String Solution


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        maybe = -1
        nlen = len(needle)
        hlen = len(haystack)
        if hlen < nlen:
            return maybe
        for s in range(len(haystack)):
            if haystack[s] == needle[0]:
                maybe = s
                for i, a in enumerate(needle):
                    if s+i > hlen-1:
                        return -1
                    elif a != haystack[s+i]:
                        s += i
                        break
                if haystack[maybe:maybe+nlen] == needle:
                    return maybe
                maybe = -1
        return maybe    
