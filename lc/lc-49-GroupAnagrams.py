# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = {}
        for s in strs:
            temp = "".join(sorted(s))
            val = ana_map.get(temp, [])
            val.append(s)
            ana_map[temp] = val
        res = []
        for k in ana_map.keys():
            res.append(ana_map[k])
        return res