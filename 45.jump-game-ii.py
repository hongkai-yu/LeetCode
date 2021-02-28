#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from math import inf

class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        steps = [inf] * (N - 1) + [0]

        for i in range(N - 2, -1, -1):
            if nums[i] == 0: continue
            steps[i] = 1 + min(steps[i + 1: i + 1 +nums[i]])
            # assert steps[i] != inf
        # print(steps)
        return steps[0]

# @lc code=end
