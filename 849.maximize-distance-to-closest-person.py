#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#

# @lc code=start
from math import inf


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dp = [0] * len(seats)

        leftDistance = inf
        for i in range(len(seats)):
            if seats[i] == 1:
                leftDistance = 0
            else:
                leftDistance += 1
                dp[i] = leftDistance


        rightDistance = inf
        for i in reversed(range(len(seats))):
            if seats[i] == 1:
                rightDistance = 0
                dp[i] = 0
            else:
                rightDistance += 1
                dp[i] = min(dp[i], rightDistance)

        # print(dp)
        return max(dp)

        
# @lc code=end

