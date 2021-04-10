#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#

# @lc code=start
from operator import itemgetter
from math import inf


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # idx = map(itemgetter(0), sorted(enumerate(arr), key = itemgetter(1)))

        # rank = 0
        # previousValue = -inf
        # for i in idx:
        #     if arr[i] > previousValue:
        #         rank += 1
        #     previousValue = arr[i]
        #     arr[i] = rank
        # return arr

        D = {j : i + 1 for i, j in enumerate(sorted(set(arr)))}
        return map(D.get, arr)
            
        
# @lc code=end

