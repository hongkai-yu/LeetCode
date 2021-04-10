#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from queue import deque


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp = [False] * (len(nums) - 1) + [True]
        # canIndices = set()
        # canIndices.add(len(nums) - 1)

        canIndices = deque([len(nums) - 1])

        for i in reversed(range(len(nums))):
            # dp[i] = any(dp[j] for j in range(i, min(i + nums[i] + 1, len(nums))))
            l, h = i, min(i + nums[i] + 1, len(nums))
            for idx in canIndices:
                if l <= idx < h:
                    canIndices.appendleft(i)
                    break
                elif idx >= h:
                    break
        
        return canIndices.popleft() == 0

# @lc code=end

