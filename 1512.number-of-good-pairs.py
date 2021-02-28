#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def numPairIndex(index: int) -> int:
            return sum([num == nums[index] for num in nums[index+1:]])
        return sum(map(numPairIndex, range(len(nums))))
        
# @lc code=end

