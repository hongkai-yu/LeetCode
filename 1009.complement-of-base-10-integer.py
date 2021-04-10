#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        ans = 0
        for i, b in enumerate(reversed(bin(N)[2:])):
            ans += (2 ** i) * (1 - int(b))
        return ans
             
        
# @lc code=end

