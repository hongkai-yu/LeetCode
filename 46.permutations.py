#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return None
        if len(nums) == 1:
            return [nums]

        res = []

        for i in range(len(nums)):
            nxtNums = nums[:i] + nums[i+1:]
            res.extend([[nums[i]] + p for p in self.permute(nxtNums)])

        # for p in permutations(nums):
        #     res.append(p)

        return res

        
# @lc code=end

