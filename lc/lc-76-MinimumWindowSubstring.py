# lc-76 Minimum Window Substring


from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        char_count = Counter(t)
        required = len(char_count)

        start = 0
        formed = 0
        window_counts ={}

        # answer tuple (Window lenght, left, right)
        ans = float("inf"), None, None

        for end, c in enumerate(s):
            window_counts[c] = window_counts.get(c,0) + 1

            if c in char_count and window_counts[c] == char_count[c]:
                formed += 1

            # Trying to shrink the window
            while start <= end and formed == required:
                c = s[start]

                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[c] -= 1
                if c in char_count and window_counts[c] < char_count[c]:
                    formed -= 1
                
                start += 1

        return "" if ans[1] is None else s[ans[1]: ans[2]+1]
