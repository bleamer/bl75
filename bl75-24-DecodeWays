# blind 75: 24 - Decode ways solution



class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1 for x in range(len(s))]
        def way_at_idx(idx, stri, memo) -> int:
            if memo[idx] != -1:
                return memo[idx]
            if idx == 0:
                if stri[idx] == '0':
                    memo[idx] = 0
                    return memo[idx]
                else:
                    memo[idx] = 1
                    return memo[idx]
            if idx == -1:
                return 1
            if stri[idx] == '0':
                if stri[idx-1] == '1' or stri[idx-1] == '2':
                    memo[idx] = way_at_idx(idx-2, stri, memo)
                    return memo[idx]
                else:
                    memo[idx] = 0
                    return memo[idx]
            ways = 0
            if (stri[idx-1] == '1') or (stri[idx-1] =='2' and int(stri[idx]) < 7):
                ways = way_at_idx(idx-1, stri, memo) + way_at_idx(idx-2, stri, memo)
            else:
                ways = way_at_idx(idx-1, stri, memo)
            memo[idx] = ways
            return ways
        return way_at_idx(len(s)-1, s, memo)        