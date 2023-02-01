from typing import (
    List,
)

class Solution:
    """
    @param flowers: the place where the flower will open in that day
    @param k:  an integer
    @return: in which day meet the requirements
    """
    def k_empty_slots(self, flowers: List[int], k: int) -> int:
        # Write your code here
        print(f'array = {flowers}, k = {k}')
        position = [0] * (len(flowers)+1)
        
        result = 1_000_000_000

        l, r = 1, k+2

        for idx, flower in enumerate(flowers):
            position[flowers[idx]] = idx
        i = 1
        while r <= len(flowers):
            if position[i] > position[l] and position[i] > position[r]:
                i+=1
                continue
            if i == r:
                result = min(result, max(position[l], position[r])+1)
            l = i
            r = i+k+1
            i += 1

        return -1 if result == 1_000_000_000 else result


sol = Solution()
print(sol.k_empty_slots([1,2,3,4], 1))
print(sol.k_empty_slots([1,3,2], 1))
print(sol.k_empty_slots([1,2,3], 1))
