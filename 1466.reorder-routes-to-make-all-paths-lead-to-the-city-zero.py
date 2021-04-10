#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(set)

        for v1, v2 in connections:
            graph[v1].add((v2, 1))
            graph[v2].add((v1, 0))
            visited = set([0])

        def dfs(u: int) -> int:
            costs = 0
            for v, c in graph[u]:
                if v in visited:
                    pass
                else:
                    visited.add(v)
                    costs += c + dfs(v)
            # print(u, costs)
            return costs
        return dfs(0)
        
# @lc code=end


if __name__ == '__main__':
    connections = [[1,0],[1,2],[3,2],[3,4]]
    n = 5
    print(Solution().minReorder(n, connections))

