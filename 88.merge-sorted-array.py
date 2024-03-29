#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[:] = sorted(nums1[:m] + nums2[:n])

        # i, j = 0, 0
        # tmp = []
        # while i < m or j < n:
        #     if i == m:
        #         tmp.extend(nums2[j:n])
        #         break
        #     if j == n:
        #         tmp.extend(nums1[i:m])
        #         break

        #     if nums1[i] <= nums2[j]:
        #         tmp.append(nums1[i])
        #         i += 1
        #     else:
        #         tmp.append(nums2[j])
        #         j += 1
        # nums1[:] = tmp

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        nums1[:n] = nums2[:n]

# @lc code=end

