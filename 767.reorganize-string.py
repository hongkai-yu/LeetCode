#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
from collections import Counter
from heapq import *


class Solution:
    def reorganizeString(self, S: str) -> str:
        res, c = [], Counter(S)
        MaxPQ = [(-freq, letter) for letter, freq in c.items()]
        heapify(MaxPQ)

        freq_max = -MaxPQ[0][0]
        if len(S) % 2 == 0 and freq_max > len(S) // 2 \
            or len(S) % 2 != 0 and freq_max > (len(S) // 2) + 1:
            return ''

        saved = None
        while MaxPQ:
            freq_neg, letter = heappop(MaxPQ)
            res.append(letter)
            freq_neg += 1

            if saved:
                heappush(MaxPQ, saved)

            if freq_neg < 0:
                saved = (freq_neg, letter)
            else:
                saved = None

        return ''.join(res)

            
# @lc code=end

