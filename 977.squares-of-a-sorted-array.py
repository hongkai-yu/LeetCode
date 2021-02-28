#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
from functools import partial
# from toolz import pipe

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # return pipe(nums, partial(map, lambda x: x * x), list, sorted)
        return sorted(list(map(lambda x: x * x, nums)))
        
# @lc code=end

if __name__ == "__main__":
    print(Solution().sortedSquares([-4, -3, 0, 1, 2]))

