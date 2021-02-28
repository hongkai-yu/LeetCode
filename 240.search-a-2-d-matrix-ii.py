#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False

        height = len(matrix)
        width = len(matrix[0])

        row = height - 1
        col = 0

        while col < width and row >= 0:
            element = matrix[row][col]
            if element == target:
                return True
            elif element > target:
                row -= 1
            else:
                col += 1
        return False

# @lc code=end
