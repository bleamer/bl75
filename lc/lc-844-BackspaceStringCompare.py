#lc 844. Backspace String Compare

from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_valid_char_index(text:str, index:int) -> int:
            backspace_count = 0
            while index >= 0:
                if text[index] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    break
                index -= 1

            return index
        p1 = len(s) -1
        p2 = len(t)-1
        while p1 >= 0 or p2 >= 0:
            p1 = get_next_valid_char_index(s, p1)
            p2 = get_next_valid_char_index(t,p2)

            if p1 >= 0 and p2 >=0:
                if s[p1] != t[p2]:
                    return False
            elif p1 >=0 or p2 >= 0:
                return False

            p1 -= 1
            p2 -= 1
        return True


            
        
        
        
        if len(s) == 0 and len(t) == 0:
            return True
        elif len(s) == 0 or len(t) == 0:
            return False
        