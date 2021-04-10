#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#

# @lc code=start
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:

        steps = 0

        while Y > X:
            steps += 1 + (Y % 2)
            Y = (Y + 1) // 2

        return steps + (X - Y)
            

# @lc code=end

