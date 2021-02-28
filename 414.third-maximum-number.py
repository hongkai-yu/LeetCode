#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
from bisect import insort

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxs = [nums.pop()]
        for num in nums:
            if num in maxs: continue
            insort(maxs, num)
            if len(maxs) > 3: maxs.pop(0)
        if len(maxs) == 3: return maxs.pop(0)
        else: return maxs.pop()
            
        
# @lc code=end

