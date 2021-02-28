#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start

from numpy import median

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        window = []
        medians = []
        for num in nums[:k]:
            window.append(num)
        medians.append(median(window))

        for num in nums[k:]:
            window.append(num)
            window.pop(0)
            medians.append(median(window))
        
        return medians

        
# @lc code=end

if __name__ == "__main__":
    print(Solution().medianSlidingWindow(
        [1,3,-1,-3,5,3,6,7], 3
    ))

