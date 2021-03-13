#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from statistics import median

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # half, nudge = divmod(len(nums1) + len(nums2), 2)
        # i = j = 0

        # while half > 0:
        #     if nums1[i] <= nums2[j]: i += 1
        #     else: j += 1
        #     value1 = min(nums1, )
        #     half -= 1

        i = j = 0
        merged = []

        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                merged += nums2[j:]
                break
            if j == len(nums2):
                merged += nums1[i:]
                break

            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j+= 1
        return median(merged)
        
# @lc code=end

