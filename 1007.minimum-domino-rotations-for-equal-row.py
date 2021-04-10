#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=start
from itertools import chain


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        swaps = {n : [0, 0] for n in range(1, 7)}

        for i in range(len(A)):
            
            dels = []
            for n in swaps:
                if n not in [A[i], B[i]]:
                    dels.append(n)
            for d in dels:
                del swaps[d]

            if len(swaps) == 0:
                return -1

            if A[i] == B[i]:
                pass
            else:
                if A[i] in swaps:
                    swaps[A[i]][1] += 1
                if B[i] in swaps:
                    swaps[B[i]][0] += 1
        
        return min(chain(*swaps.values()))

        
# @lc code=end

