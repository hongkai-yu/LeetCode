#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from functools import reduce

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0], reverse = True)
        
        res = []
        workingInterval = intervals.pop()

        while intervals:
            newInterval = intervals.pop()
            if newInterval[0] <= workingInterval[1]:
                workingInterval[1] = max(newInterval[1], workingInterval[1])
            else:
                res.append(workingInterval)
                workingInterval = newInterval

        res.append(workingInterval)
        return res

# @lc code=end

