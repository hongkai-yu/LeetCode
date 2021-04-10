#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from math import prod


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prodWithoutZeros = 1
        # numZeros = 0
        # for n in nums:
        #     if n == 0:
        #         numZeros += 1
        #     else:
        #         prodWithoutZeros *= n

        numZeros = nums.count(0)
        prodWithoutZeros = prod(n for n in nums if n != 0)
        
        if numZeros > 1:
            return [0] * len(nums)
        elif numZeros == 1:
            return [prodWithoutZeros if n == 0 else 0 for n in nums]
        else:
            return [prodWithoutZeros // n for n in nums]
# @lc code=end

