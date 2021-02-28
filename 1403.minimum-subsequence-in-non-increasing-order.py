#
# @lc app=leetcode id=1403 lang=python3
#
# [1403] Minimum Subsequence in Non-Increasing Order
#

# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        bar = sum(nums) / 2        
        nums.sort(reverse = True)

        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s > bar: return nums[:i+1]
        
        return []

        
# @lc code=end