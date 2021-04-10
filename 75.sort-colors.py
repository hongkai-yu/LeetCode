#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            elif nums[i] == nums[j]:
                foundDiff = False
                for k in range(i + 1, j):
                    if nums[k] < nums[i]:
                        foundDiff = True
                        nums[i], nums[k] = nums[k], nums[i]
                        break
                    elif nums[k] > nums[i]:
                        foundDiff = True
                        nums[j], nums[k] = nums[k], nums[j]
                        break
                    else:
                        pass
                if not foundDiff:
                    break
            else:
                pass

            if nums[i] == 0:
                i += 1
            if nums[j] == 2:
                j -= 1
        
# @lc code=end

