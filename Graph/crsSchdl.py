# 207. Course Schedule

# There are a total of numCourses courses you have to take,
# labeled from 0 to numCourses - 1. You are given an array 
# prerequisites where prerequisites[i] = [ai, bi] indicates 
# that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return true if you can finish all courses. Otherwise, return false.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# Constraints:
#     1 <= numCourses <= 2000
#     0 <= prerequisites.length <= 5000
#     prerequisites[i].length == 2
#     0 <= ai, bi < numCourses
#     All the pairs prerequisites[i] are unique.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to its prerequisites
        courseDict = collections.defaultdict(list)
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[nextCourse].append(prevCourse)

        # visit each course
        visited = set()
        def dfs(course):
            # return False if we are back to a course we've visited before
            if course in visited:
                return False
            # return True if we've reached a course with no prerequisites
            if courseDict[course] == []:
                return True

            # mark this course as visited
            visited.add(course)
            # visit all the prerequisites of this course
            for prevCourse in courseDict[course]:
                # if any of the prerequisites can't be visited, return False
                if not dfs(prevCourse):
                    return False
            # all prerequisites can be visited, return True
            return True