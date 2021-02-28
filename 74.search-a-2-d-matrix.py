#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def searchRow(rows: list[list[int]], target: int) -> list[int]:

            if rows == []: return False

            center = len(rows) // 2

            if rows[center] == []: return False

            if target < rows[center][0]:
                return searchRow(rows[:center], target)
            elif target > rows[center][-1]:
                return searchRow(rows[center + 1:], target)
            else:
                return searchCol(rows[center], target)

        def searchCol(cols: list[int], target: int) -> bool:

            if cols == []: return False

            center = len(cols) // 2

            if target == cols[center]: return True
            elif target < cols[center]:
                return searchCol(cols[:center], target)
            else:
                return searchCol(cols[center + 1:], target)

        return searchRow(matrix, target)
        
# @lc code=end
if __name__ == "__main__":
    output = Solution().searchMatrix([[1,3,5]], 4)
    print(output)

