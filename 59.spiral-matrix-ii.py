#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
import numpy as np

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dx = [1, 0, -1, 0] # E, S, W, N
        dy = [0, 1, 0, -1] # E, S, W, N
        x = y = di = 0

        matrix = np.zeros((n, n))

        for i in range(n * n):
            matrix[x][y] = i + 1

            if (x + dx[di] >= n
                or y + dy[di] >= n
                or matrix[x + dx[di]][y + dy[di]] != 0
            ):  di = (di + 1) % 4
            
            x += dx[di]
            y += dy[di]
            
        return matrix.astype(int).T.tolist()
            


        
# @lc code=end

