
# lc 207 - Course Schedule
from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        p_dict = defaultdict(list)
        num_course_dep = [0]*numCourses

        for crs, preq in prerequisites:
            p_dict[preq].append(crs)
            num_course_dep[crs] += 1

        print(p_dict)
        queue = deque()
        compleleted_courses  = 0
        # courses with no dependency
        for crs in range(0,numCourses):
            if num_course_dep[crs] == 0:
                queue.append(crs)
        while(queue):
            crs = queue.popleft()
            compleleted_courses += 1
            if crs in p_dict:
                dep_courses = p_dict[crs]
                for dep_course in dep_courses:
                    num_course_dep[dep_course] -= 1
                    if num_course_dep[dep_course] == 0:
                        queue.append(dep_course)
        

        return compleleted_courses == numCourses
