#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
from math import inf

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # first, second = inf, inf
        # for n in nums:
        #     if n <= first:
        #         first = n
        #     elif n <= second:
        #         second = n
        #     else:
        #         return True
        # return False

        first = inf
        for i in range(len(nums)):
            first = min(first, nums[i])
            second = inf
            for j in range(i + 1, len(nums)):
                if nums[j] > second:
                    return True
                elif nums[j] <= first:
                    pass
                else:
                    second = min(second, nums[j])
        return False

        
# @lc code=end

