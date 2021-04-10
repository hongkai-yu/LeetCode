#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums: List[int], path: List[int], res: List[List[int]]):
        if not nums:
            res.append(path)

        visited = set()
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
                self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)

        
# @lc code=end

