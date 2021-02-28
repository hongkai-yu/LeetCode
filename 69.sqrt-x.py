#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        # return 2
        return int(math.floor(math.sqrt(x)))

# @lc code=end

if __name__ == '__main__':
    print(Solution().mySqrt(4))