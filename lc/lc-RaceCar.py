# LC 818 Race Car


import collections

class Solution:
    def racecar(self, target: int) -> int:
        #initialize steps, position, velocity (speed with direction)
        queue = collections.deque([(0, 0, 1)])

        while queue:
            steps, pos, vel = queue.popleft()

            if pos == target:
                return steps

            # if are in the direction of target continue in that direction
            queue.append((steps+1, pos+vel, 2*vel))

            # reverse the direction if we are moving away from the target
            # or if we will cross the target in next step
            if (pos+vel > target and vel > 0) or (pos+vel < target and vel < 0):
                queue.append((steps+1, pos, -vel/abs(vel)))
        
