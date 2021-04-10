#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        leftSum = 0
        rightSum = sum(nums[1:])

        if leftSum == rightSum:
            return 0

        for pivot in range(1, len(nums)):
            leftSum += nums[pivot - 1]
            rightSum -= nums[pivot]
            if leftSum == rightSum:
                return pivot
        return -1
        
# @lc code=end

