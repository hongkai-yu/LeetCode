#
# @lc app=leetcode id=1573 lang=python3
#
# [1573] Number of Ways to Split a String
#

# @lc code=start
from itertools import accumulate

class Solution:
    def numWays(self, s: str) -> int:

        s = [int(c) for c in s] 

        si, mod = divmod(sum(s), 3)

        if mod != 0:
            return 0

        if si == 0:
            return ((len(s) - 1) * (len(s) - 2) // 2) % (10**9 + 7) # choose two from len(l) - 1 breaks
        
        cut1, cut2 = 0, 0
        total = 0
        for num in s:
            total += num
            if total == si:
                cut1 += 1
            elif total == si * 2:
                cut2 += 1
            else:
                pass

        # cumsum = accumulate(s)
        # cut1, cut2 = 0, 0
        # for c in cumsum:
        #     if c == si:
        #         cut1 += 1
        #     elif c == si * 2:
        #         cut2 += 1
        #     else:
        #         pass
        
        return (cut1 * cut2) % (10**9 + 7)
        
# @lc code=end

