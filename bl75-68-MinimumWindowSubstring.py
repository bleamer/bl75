# blind 75: 68 - Minimum Window Substring solution
# LC347. Minimum Window Substring


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for i in range(len(nums)+1)]
        count ={}
        for n in nums:
            count[n] = count.get(n,0) + 1
        for keys, values in count.items():
            freq[values].append(keys)
        final  = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                final.append(num)
                if len(final) == k:
                    return final