#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            maxSub = max(nums[i], maxSub)
        return maxSub



        
# @lc code=end


