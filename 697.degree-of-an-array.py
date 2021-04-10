#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        numDict = dict() # (freq, start, end)
        for i, n in enumerate(nums):
            if nums[i] not in numDict:
                numDict[n] = [1, i, i]
            else:
                numDict[n][0] = numDict[n][0] + 1
                numDict[n][2] = i

        degree = max(numDict[n][0] for n in nums)

        return min(v[2] - v[1] + 1 for v in numDict.values() if v[0] == degree)
        
        # return min(map(lambda x: x[2] - x[1] + 1, 
        #            filter(lambda n: n[0] == degree, numDict.values())))


        
# @lc code=end

