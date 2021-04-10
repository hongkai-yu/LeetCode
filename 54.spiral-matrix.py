#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        di, dj = 0, 1

        m = len(matrix)
        n = len(matrix[0])

        res = []
        visited = set()

        while True:
            if 0 <= i < m and 0 <= j < n and i * n + j not in visited:
                res.append(matrix[i][j])
                visited.add(i * n + j)
            else:
                break

            if 0 <= i + di < m and 0 <= j + dj < n and (i + di) * n + (j + dj) not in visited:
                pass
            else:
                # turn right
                di, dj = dj, -di

            i += di; j += dj
        return res
        
# @lc code=end

