#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        mid = len(nums) // 2
        
        return min(self.findMin(nums[:mid]), self.findMin(nums[mid:]))
        
# @lc code=end

