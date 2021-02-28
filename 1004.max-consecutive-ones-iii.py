#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from operator import countOf


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if len(A) == 0: return 0
        
        start = end = 0
        nZeros = 0

        for i in range(len(A)):
            if A[end] == 0: nZeros += 1
            end += 1

            if nZeros > K:
                if A[start] == 0: nZeros -= 1
                start += 1
        return end - start



        
# @lc code=end

