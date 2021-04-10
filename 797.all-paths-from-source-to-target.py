#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.dfs(0, graph, [], res)
        return res

    def dfs(self, node: int, graph: List[List[int]], path: List[int], res: List[List[int]]) -> None:
        path.append(node)
        if node == len(graph) - 1:
            res.append(path.copy())
            path.pop()
            return
        
        for nxtNode in graph[node]:
            self.dfs(nxtNode, graph, path, res)
        path.pop()


        
# @lc code=end

