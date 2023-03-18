
# blind75:13 - Group Anagrams solution
# LC49. Group Anagrams


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        smap = {}
        for s in strs:
            t = "".join(sorted(s))
            value = smap.get(t)
            if not value:
                value = []
            value.append(s)
            smap[t] = value
            # print(smap)
        retVal=[]
        for valueList in smap.values():
            retVal.append(valueList)
        return retVal

