
# blind75:13 - Group Anagrams Ordinal value solution
# LC49. Group Anagrams


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hashana(s):
            l = [0] * 26
            for c in s:
                l[ord(c)-ord('a')]+=1
            return tuple(l)
        smap = defaultdict(list)
        for s in strs:
            t = hashana(s)
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

