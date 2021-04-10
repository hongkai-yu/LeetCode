#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # N = len(matrix) - 1

        # for i in range(N // 2 + 1):
        #     for j in range(i, N - i):
        #         # print(i, j)
        #         matrix[i][j], matrix[j][N-i], matrix[N-i][N-j], matrix[N-j][i] = (
        #             matrix[N-j][i], matrix[i][j], matrix[j][N-i], matrix[N-i][N-j])

        matrix[:] = map(list, zip(*matrix[::-1]))
        
# @lc code=end

