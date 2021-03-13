#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        remainings = {}
        for index, num in enumerate(nums):
            if num in remainings:
                return [index, remainings[num]]
            remainings[target - num] = index


        # remainings = {}
        # for index, num in enumerate(nums):
        #     remainings[target - num] = index
        
        # for index, num in enumerate(nums):
        #     if num in remainings and index != remainings[num]:
        #         return [index, remainings[num]]
        
        # return None

# @lc code=end

