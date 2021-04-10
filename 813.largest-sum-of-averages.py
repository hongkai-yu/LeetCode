#
# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#

# @lc code=start
from functools import lru_cache
from statistics import mean


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:

        @lru_cache(maxsize=len(A)*K)
        def dfs(idx: int, K: int) -> float:
            if idx >= len(A) or len(A) - idx < K:
                return -1
            if K == 1:
                return meanCache(idx, len(A))
            return max(meanCache(idx, i) + dfs(i, K - 1)
                       for i in range(idx + 1, len(A)) if dfs(i, K - 1) != -1)

        @lru_cache(maxsize = len(A) * len(A) // 2)
        def meanCache(i: int, j: int):
            return mean(A[i : j])

        return dfs(0, K)
        
# @lc code=end

