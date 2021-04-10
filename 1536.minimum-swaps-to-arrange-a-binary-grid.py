#
# @lc app=leetcode id=1536 lang=python3
#
# [1536] Minimum Swaps to Arrange a Binary Grid
#

# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:

        n = len(grid)

        tailZeros = [] # number of zeros in tail

        for row in grid:
            if 1 not in row:
                tailZeros.append(n)
            else:
                tailZeros.append(row[::-1].index(1))

        ans = 0
        for i in range(n):
            target = n - 1 - i 
            if tailZeros[i] >= target:
                pass
            else:
                swaped = False
                for j in range(i + 1, n):
                    if tailZeros[j] >= target:
                        ans += j - i
                        tailZeros[i + 1 : j + 1] = tailZeros[i: j]
                        swaped = True
                        break
                if not swaped:
                    return -1
        return ans
                        
# @lc code=end

