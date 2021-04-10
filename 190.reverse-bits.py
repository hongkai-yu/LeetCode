#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
from functools import lru_cache


class Solution:
    def reverseBits(self, n: int) -> int:

        # binary = bin(n)[2:]
        # binary = '0' * (32 - len(binary)) + binary 
        binary = '{:032b}'.format(n)

        return sum(map(lambda e: int(e[1]) * self.exp2(e[0]), enumerate(binary)))


    @lru_cache(maxsize=32)
    def exp2(self, x: int) -> int:
        if x == 0:
            return 1

        return 2 * self.exp2(x - 1)
        
# @lc code=end

