#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    def numTilings(self, N: int) -> int:
        div, mod = divmod(N, 3)

        return (5 ** div * max(1, mod)) % (10 ** 9 + 7)
        
# @lc code=end

