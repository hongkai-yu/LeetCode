#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
from functools import reduce


class Solution:
    def addDigits(self, num: int) -> int:

        # rem = num % 9

        # if rem == 0:
        #     if num == 0: return 0
        #     else:        return 9
        # else:            return rem

        if num < 10: return num
        
        return self.addDigits(reduce(lambda a, b: int(a) + int(b), str((num))))
            
        
        
# @lc code=end

