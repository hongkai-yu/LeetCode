#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # states: clear, hold, aftersell
        states = {'clear': 0, 'hold': -prices[0], 'cooldown': -inf}

        # actions: buy (clear -> hold) sell (hold -> cooldown) rest (cooldown -> clear; stay hold/clear)

        for p in prices:
            nxtStates = {}
            nxtStates['clear'] = max(states['clear'], states['cooldown'])
            nxtStates['hold'] = max(states['hold'], states['clear'] - p)
            nxtStates['cooldown'] = states['hold'] + p
            states = nxtStates
        
        return max(states.values())

        
# @lc code=end

