#
# @lc app=leetcode id=1320 lang=python3
#
# [1320] Minimum Distance to Type a Word Using Two Fingers
#

# @lc code=start
from typing import List
from math import inf
from functools import cache

class Solution:
    def minimumDistance(self, word: str) -> int:

        word = list(map(lambda c: ord(c) - ord('A'), word))

        @cache
        def d(c1: int, c2: int) -> int:
            if c1 == -1 or c2 == -1:
                return 0
            return abs(c1 // 6 - c2 // 6) + abs(c1 % 6 - c2 % 6)
        
        dp = {(word[0], -1) : 0} # -1 means off board

        for nxtc in word[1:]:
            nxtdp = {}
            for (c1, c2) in dp:
                nxtdp[nxtc, c2] = min(dp[c1, c2] + d(c1, nxtc), nxtdp.get((nxtc, c2), inf))
                nxtdp[c1, nxtc] = min(dp[c1, c2] + d(c2, nxtc), nxtdp.get((c1, nxtc), inf))
            dp = nxtdp
            # print(dp)
        
        return min(dp.values())

# @lc code=end

if __name__ == '__main__':
    word = 'HAPPY'
    print(Solution().minimumDistance(word))

