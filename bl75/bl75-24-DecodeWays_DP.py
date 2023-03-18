# bl75-24-Decode Ways Dynamic Programming Solution


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        if s[0] == '0':
            return 0
        else:
            dp[1] = 1
        
        for idx in range(2, len(s)+1):
            if s[idx-1] == '0':
                if s[idx-2] == '1' or s[idx-2] == '2':
                    dp[idx] = dp[idx-2]
                else:
                    return 0
            else:
                if (s[idx-2] == '1') or (s[idx-2] =='2' and int(s[idx-1]) < 7):
                    dp[idx] =  dp[idx-1] + dp[idx-2]
                else:
                    dp[idx] = dp[idx-1]

        return dp[len(s)]