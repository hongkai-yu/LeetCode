#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])
        if r * c != m * n: return nums

        ans = [[0] * c for _ in range(r)]

        for i in range(m * n):
            ans[i // c][i % c] = nums[i // n][i % n]

        return ans
            
        
# @lc code=end

