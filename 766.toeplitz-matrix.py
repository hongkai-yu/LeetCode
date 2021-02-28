#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#


# @lc code=start
from itertools import chain


class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        startPoints = ({(0, j) for j in range(n-1)} 
                      | {(i, 0) for i in range(m-1)})

        for x, y in startPoints:
            value = matrix[x][y]
            i, j = x + 1, y + 1
            while(i < m and j < n):
                if matrix[i][j] != value: return False
                i, j = i + 1, j + 1

        return True
        
# @lc code=end

if __name__ == "__main__":
    assert Solution().isToeplitzMatrix([[58],[46],[15],[55],[55],[25]])
    assert Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]
)
