#
# @lc app=leetcode id=1442 lang=python3
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#

# @lc code=start
from operator import __xor__
from functools import reduce
from itertools import combinations, accumulate

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        arr.insert(0,0)
        N = len(arr)
        prefix = list(accumulate(arr, __xor__))
        # print(prefix)

        cnt = 0
        for i, k in combinations(range(N), 2):
            # print(i, k)
            if prefix[i] == prefix[k]:
                cnt += k - i - 1

        return cnt


        # @cache
        # def xorReduce(p: int, q: int) -> int:
        #     return reduce(__xor__, arr[p: q+1])

        # cnt = 0
        # for i in range(0, N):
        #     for j in range(i + 1, N):
        #         for k in range(j, N):
        #             if xorReduce(i, j - 1) == xorReduce(j, k):
        #                 cnt += 1

        # return cnt
                        
                    
        
# @lc code=end

