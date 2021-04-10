#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict
from typing import List
from math import inf
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        nodeNeighbours = defaultdict(set)
        for u, v, t in times:
            nodeNeighbours[u].add((v, t))

        visitTime = [inf] * (n + 1)
        visited = set()

        minPQ = [(0, k)]
        visitTime[k] = 0
        
        while minPQ:
            t, start = heappop(minPQ)
            if start in visited:
                continue
            visited.add(start)
            if len(visited) == n:
                return t
            
            for end, tt in nodeNeighbours[start]:
                if t + tt < visitTime[end]:
                    visitTime[end] = t + tt
                    heappush(minPQ, ((t + tt), end))
        return -1

        # def dfs(start: int, time: int) -> None:

        #     visitTime[start] = time

        #     for end, t in nodeNeighbours[start]:
        #         if visitTime[end] > time + t:
        #             dfs(end, time + t)

        # dfs(k, 0)
        # totalTime = max(visitTime.values())
        # return -1 if totalTime == inf else totalTime
                
        
# @lc code=end

