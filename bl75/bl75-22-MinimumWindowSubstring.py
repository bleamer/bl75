# blind 75: 22 - Minimum Window Substring solution
# LC76. Minimum Window Substring



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        
        
        tmap, nmap = {},{}
        for c in t:
            tmap[c] = 1 + tmap.get(c,0)

        found, want = 0, len(tmap)
        final_ss = [-1, -1]
        anslen = float('inf')
        left = 0
        for right in range(len(s)):
            # Starting from left slide right end of window
            c = s[right]
            nmap[c] = 1 + nmap.get(c, 0)

            # no. of characters in t vs. what we have encountered so far
            if c in tmap and nmap[c] == tmap[c]:
                found += 1
            
            while found == want:
                if (right-left+1) < anslen:
                    final_ss = [left, right]
                    anslen = right - left + 1
                # remove left most found character to check if can be found later
                # and reduce its found count
                nmap[s[left]] -= 1
                if s[left] in tmap and nmap[s[left]] < tmap[s[left]]:
                    found -= 1
                left += 1
        left, right = final_ss
        return s[left:right+1] if anslen != float('inf') else ""

