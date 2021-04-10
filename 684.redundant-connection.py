#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}

        def find(v: int) -> int:
            if v not in parent:
                parent[v] = v
            while v != parent[v]:
                v = parent[v]
            return v

        for e in edges:
            p1, p2 = find(e[0]), find(e[1])

            if p1 == p2:
                return e
            else:
                parent[p2] = p1

        raise ValueError("Nothing to remove")


# @lc code=end

