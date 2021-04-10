#
# @lc app=leetcode id=1497 lang=python3
#
# [1497] Check If Array Pairs Are Divisible by k
#

# @lc code=start
from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod = Counter(map(lambda x: x % k, arr))

        if mod[0] % 2 != 0:
            return False

        if k % 2 == 0:
            if mod[k // 2] % 2 != 0:
                return False

        for i in range(1, (k + 1) // 2):
            if mod[i] != mod[k - i]:
                return False


        return True
        
# @lc code=end

