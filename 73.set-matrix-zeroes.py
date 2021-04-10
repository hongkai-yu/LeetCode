#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from itertools import product

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        
        rowMult = [0 if 0 in row else 1 for row in matrix]
        colMult = [0 if 0 in col else 1 for col in zip(*matrix)]

        for i, j in product(range(m), range(n)):
            matrix[i][j] *= rowMult[i] * colMult[j]

        
# @lc code=end

