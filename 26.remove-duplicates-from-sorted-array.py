#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = None

        i = 0
        while True:
            if i >= len(nums): break
            if nums[i] == seen:
                del nums[i]
            else:
                seen = nums[i]
                i += 1
        return len(nums)

        
# @lc code=end

if __name__ == '__main__':
    nums = [1,1,2]
    print(Solution().removeDuplicates(nums))
