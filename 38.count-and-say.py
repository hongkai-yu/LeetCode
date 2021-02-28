#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=31)
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        
        prevSay = self.countAndSay(n - 1)
        
        counter = 0
        prevDigit = ''
        output = ''
        for digit in prevSay:
            if digit == prevDigit: counter += 1
            else:
                if counter > 0: output += str(counter) + prevDigit
                prevDigit = digit
                counter = 1
        if counter > 0: output += str(counter) + prevDigit

        return output

# @lc code=end

