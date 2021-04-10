#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = {0: 1}

        for n in nums:
            nxtDp = {}
            for cur in dp:
                nxtDp[cur + n] = nxtDp.get(cur + n, 0) + dp[cur]
                nxtDp[cur - n] = nxtDp.get(cur - n, 0) + dp[cur]
            dp = nxtDp
        return dp.get(S, 0)

        
# @lc code=end

