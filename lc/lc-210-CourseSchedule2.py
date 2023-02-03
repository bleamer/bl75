# lc-210: Course Schedule 2 solution


from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for course, preq in prerequisites:
            graph[course].append(preq)

        
        stack = []
        visited, cycle = set(), set()

        def dfs(course):
            '''
            checks if the all the dependencies are satisfied recursively
            '''
            # Return false for entire dfs if a cycle is detected
            # cycle set keeps tracks of courses that on the prerequisite path from source node
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            # Recursive walk through and add preq in given source course
            # if we encounter a course more than once on discovery path that means
            # there is circular dependency
            for preq in graph[course]:
                if not dfs(preq): # detected cycle
                    return False
            cycle.remove(course)
            visited.add(course)
            stack.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []

        return stack