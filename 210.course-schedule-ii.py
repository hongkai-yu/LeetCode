#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = {i : set() for i in range(numCourses)}

        for u, v in prerequisites:
            graph[u].add(v)

        res = [] 
        state = [0] * numCourses

        def dfs(course: int) -> bool:
            if state[course] == 2:
                return True
            elif state[course] == 1:
                return False
            else:
                state[course] = 1
                for preq in graph[course]:
                    if not dfs(preq):
                        return False
                state[course] = 2
                res.append(course)
                return True

        for course in graph:
            if not dfs(course):
                return []

        return res
        
# @lc code=end

if __name__ == "__main__":
    preqs = [[1,0]]
    print(Solution().findOrder(2, preqs))

