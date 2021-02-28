#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return list(map(lambda t: t[1], sorted(
            [(sum(row), index) for index, row in enumerate(mat)]
        )))[:k]

# @lc code=end
