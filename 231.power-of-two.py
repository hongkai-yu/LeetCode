#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
# from functools import cache
from math import log2


# @cache
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False

        return log2(n).is_integer()

        # if n == 1:
        #     return True
        # elif n <= 0:
        #     return False
        # else:
        #     div, mod = divmod(n, 2)
        #     return mod == 0 and self.isPowerOfTwo(div)
        
# @lc code=end

