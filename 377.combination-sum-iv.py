#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start

from functools import cache

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        nums = list(filter(lambda x: x <= target, nums))
        if not nums:
            return 0

        nums.sort()

        @cache
        def dfs(curSum: int) -> int: 

            if curSum == target:
                return 1
            elif curSum > target:
                return 0
            else:
                res = 0
                for n in nums:
                    res += dfs(n + curSum)
                    if n + curSum >= target: 
                        break
                return res

        return dfs(0)
        
# @lc code=end

