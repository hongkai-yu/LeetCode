#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        symbolNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        nums = [symbolNum[c] for c in s] + [0]

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]: nums[i] = -nums[i]
        
        return sum(nums)

# @lc code=end

