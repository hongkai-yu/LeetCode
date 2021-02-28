#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        N = len(mat)
        for i in range(N):
            sum += mat[i][i]
            sum += mat[i][N-1-i]
        if (N - 1) % 2 == 0:
            c = int((N-1)/2)
            sum -= mat[c][c]
        return sum
        
# @lc code=end

