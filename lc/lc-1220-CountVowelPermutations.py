# lc 1220 Count Vowels Permutation


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # ae
        # ea or ei
        # ia ie io iu
        # oi ou
        # ua 

        # build a trie
        # do dfs, each node storing count of 

        # ncm = {'a':['e'],
        #         'e':['a','i'],
        #         'i':['a','e','o','u'],
        #         'o':['i', 'u'],
        #         'u':['a']
        #         }
        memo = {}
        def counter(prevc:str, l:int) -> int:
            if l == 1:
                return 1
            
            if (prevc, l) in memo:
                return memo[(prevc, l)]
            if prevc =='a':
                ret = counter('e', l-1)
            if prevc =='e':
                ret = counter('a', l-1) + counter('i', l-1)
            if prevc =='i':
                ret = counter('a', l-1) + counter('e', l-1) + counter('o', l-1)+ counter('u', l-1)
            if prevc =='o':
                ret = counter('i', l-1) + counter('u', l-1)
            if prevc =='u':
                ret = counter('a', l-1)
            memo[(prevc, l)] = ret
            
            return ret
        
        if n == 1:
           return 5
        total = 0
        for c in 'aeiou':
            total += counter(c, n)
        # return total
        return int(total % (10**9+7))
    

import unittest
class Tests(unittest.TestCase):
    def test_t1(self):
        s = Solution()
        inp, exp = 2, 10
        op = s.countVowelPermutation(inp)
        self.assertEquals(exp, op)

    def test_t2(self):
        s = Solution()
        inp, exp = 5, 68
        op = s.countVowelPermutation(inp)
        self.assertEquals(exp, op)


unittest.main()