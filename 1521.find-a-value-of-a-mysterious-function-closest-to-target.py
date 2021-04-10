#
# @lc app=leetcode id=1521 lang=python3
#
# [1521] Find a Value of a Mysterious Function Closest to Target
#

# @lc code=start
from math import inf

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        dp = set()
        res = inf
        for num in arr:
            dp = {num & state for state in dp} | {num}
            res = min(res, min(abs(newState - target) for newState in dp))
        return res

        
# @lc code=end

