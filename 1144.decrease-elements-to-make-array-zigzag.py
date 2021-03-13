#
# @lc app=leetcode id=1144 lang=python3
#
# [1144] Decrease Elements To Make Array Zigzag
#

# @lc code=start
from typing import List
from math import inf

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:

        nums = [inf] + nums + [inf]
        diff = [0, 0]

        for i in range(1, len(nums) - 1):
            diff[i % 2] += max(nums[i] - min(nums[i-1], nums[i+1]) + 1, 0)

        return min(diff)
            
        # diffEven = diffOdd = 0
        # for i in range(0, len(nums)):
        #     if i == 0: minNeighour = nums[i+1]
        #     elif i == len(nums) - 1: minNeighour = nums[i-1]
        #     else: minNeighour = min(nums[i-1], nums[i+1])
        #     diff = max(nums[i] - minNeighour + 1, 0)

        #     if i % 2 == 0: diffEven += diff
        #     else: diffOdd += diff

        # return min(diffEven, diffOdd)
# @lc code=end

if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [9,6,1,6,2]

    print(Solution().movesToMakeZigzag(nums1), 'answer')
    print(Solution().movesToMakeZigzag(nums2), 'answer')

