#
# @lc app=leetcode id=1042 lang=python3
#
# [1042] Flower Planting With No Adjacent
#

# @lc code=start

class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        connected = [[] for _ in range(n)]
        for x, y in paths:
            connected[x - 1].append(y - 1)
            connected[y - 1].append(x - 1)
        
        flowers = [0] * n
        for i in range(n):
            flowers[i] = ({1, 2, 3, 4} - {flowers[i] for i in connected[i]}).pop()

        return flowers

# @lc code=end

if __name__ == '__main__':
    print(Solution().gardenNoAdj(
        10, []
        ))