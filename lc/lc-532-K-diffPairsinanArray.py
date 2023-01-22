# lc532. K-diff Pairs in an Array


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
   
        def binary_search(arr, low, high, key) -> int:
            # print(arr, low, high, key)
            l,h = low, high
            while l <= h:
                mid = (l + h) // 2
                if key == arr[mid]:
                    # print('found', mid, l, h)
                    return mid
                if key < arr[mid]:
                    h = mid-1
                else:
                    l = mid+1
            return -1
            
        result = set()
        snums = sorted(nums)
        l, r = 0, len(snums)
        for i, c in enumerate(snums):
            searchKey = c-k
            # print('dfas', c, k, searchKey)
            if (ret := binary_search(snums, 0, len(snums)-1, searchKey)) >= 0 and ret != i:
                result.add((c,c-k))
        return len(result)