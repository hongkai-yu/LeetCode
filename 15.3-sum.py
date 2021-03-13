#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start

from typing import List

from bisect import bisect_left


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i-1]: continue

            l = i + 1; r = len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while True:
                        l += 1
                        if l >= r or nums[l] != nums[l-1]: break
                    while True:
                        r -= 1
                        if l >= r or nums[r] != nums[r+1]: break

        return res

        #     twoSum = -nums[i]
        #     for j in range(i):
        #         key = twoSum - nums[j]
        #         index = bisect_left(nums[:j], key)
        #         if nums[i] == 4 and nums[j] == -2:
        #             print(key)
        #         if index < j and nums[index] == key:
        #             l = [key, nums[j], nums[i]]
        #             h = self.hash(l)
        #             if h not in found:
        #                 res.append(l)
        #                 found.add(h)
        # return res

    # def hash(self, l: List[int]) -> int:
    #     a, b, c = l[0], l[1], l[2]
    #     return a + b * 7 + c * 77
                
# @lc code=end

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    nums = [0, 0, 0, 0]
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(Solution().threeSum(nums))

