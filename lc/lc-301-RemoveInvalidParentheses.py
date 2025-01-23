# lc 301 Remove Invalid Parentheses

from collections import deque
class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(s):
            # check if the string has balanced '()'
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0: # More closing parentheses than opening ones
                    return False

            return count == 0 # Balanced parentheses if count is zero
        
        # BFS approach to find all valid strings with minimum removal
        result = []
        visited = set()  # To avoid processing the same string multiple times
        queue = deque([s])
        visited.add(s)
        found = False # Flag to stop our BFS when found some valid strings
        
        while queue:
            curr = queue.popleft()
            if is_valid(curr):
                found = True
                result.append(curr)

            # if found some some valid string, do not go further in this branch of bfs
            if found:
                continue
            
            # Generate all possible string removing one paranthesis at a time
            for idx, c in enumerate(curr):
                if c not in "()": # look for char other than ()
                    continue
                # we found a ( or ), remove that parantheses and create
                # a new string
                new_s = curr[:idx] + curr[idx+1:]
                if new_s not in visited:
                    visited.add(new_s)
                    queue.append(new_s) # append this string to be explored later
        return result


"""
    n the worst case, we generate all 2n2n strings and check the validity of each string. Each check takes O(n)O(n), so the total time complexity is:
    O(2n⋅n)
    O(2n⋅n)

This is an exponential time complexity, as we might need to generate and check all possible combinations of parentheses.

Time complexity: O(2n⋅n)
Space complexity: O(2n⋅n)
"""