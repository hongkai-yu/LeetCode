#
# @lc app=leetcode id=1551 lang=python3
#
# [1551] Minimum Operations to Make Array Equal
#

# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 != 0:
            # 2 + 4 + 6 + ... = (1 + size) * size
            size = n // 2
            return int((1 + size) * size)
        else:
            # 1 + 3 + 5 + ... = (1 + (2 * size - 1)) * size / 2
            size = n // 2
            return int((1 + (2 * size - 1)) * size / 2)
        
# @lc code=end

