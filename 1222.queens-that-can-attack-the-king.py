#
# @lc app=leetcode id=1222 lang=python3
#
# [1222] Queens That Can Attack the King
#

# @lc code=start
from itertools import product


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        queens = set(map(tuple, queens))

        res = []

        for dx, dy in product((-1, 0, 1), repeat = 2):
            if (dx, dy) == (0, 0):
                continue
            x, y = king

            while True:
                x += dx
                y += dy
                if not ((0 <= x <= 7) and (0 <= y <= 7)):
                    break
                elif (x, y) in queens:
                    res.append([x, y])
                    break
        return res

# @lc code=end

