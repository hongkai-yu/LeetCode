#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from bisect import bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
                
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
            

    #     # print(nums)

    #     if nums[0] <= nums[len(nums) - 1]:
    #         return self.binarySearch(nums, target)

    #     mid = len(nums) // 2
    #     if nums[0] < nums[mid]:
    #         if nums[0] <= target < nums[mid]:
    #             return self.search(nums[:mid], target)
    #         else:
    #             result = self.search(nums[mid:], target)
    #             return mid + result if result != -1 else -1
    #     else:
    #         if nums[mid] <= target <= nums[len(nums) - 1]:
    #             result =  self.search(nums[mid:], target)
    #             return mid + result if result != -1 else -1
    #         else:
    #             return self.search(nums[:mid], target)

    # def binarySearch(self, nums: List[int], target: int) -> int:
    #     # print(nums)
    #     i = bisect_left(nums, target)

    #     if i != len(nums) and nums[i] == target:
    #         return i
    #     else:
    #         return -1


# @lc code=end

if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [1, 3]

    target = 0
    # target = 1
    print(Solution().search(nums, target))