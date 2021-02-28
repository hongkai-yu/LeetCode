#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
from collections import defaultdict
from operator import itemgetter


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbours = defaultdict(set)
        for start, end in edges:
            neighbours[start].add(end)
            neighbours[end].add(start)
        
        yetVisited = set(range(n))
        leaves = {node for node in neighbours if len(neighbours[node]) == 1}


        while (len(yetVisited) > 2):
            yetVisited -= leaves
            newLeaves = set()
            for leaf in leaves:
                # assert len(neighbours[leaf]) == 1
                branch = neighbours[leaf].pop()
                neighbours[branch].remove(leaf)
                if len(neighbours[branch]) == 1:
                    newLeaves.add(branch)
                # del neighbours[leaf]
            leaves = newLeaves

        return list(yetVisited)
# @lc code=end

