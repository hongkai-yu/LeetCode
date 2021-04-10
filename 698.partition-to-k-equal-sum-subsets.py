#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        target, mod = divmod(sum(nums), k)
        if mod != 0:
            return False

        nums.sort(reverse = True)
        groupTarget = [target] * k

        
        def dfs(pos: int) -> bool:
            if pos == len(nums):
                return True
            n = nums[pos]
            for i in range(k):
                if i != 0 and groupTarget[i] == groupTarget[i - 1]:
                    continue

                if groupTarget[i] >= n:
                    groupTarget[i] -= n
                    if dfs(pos + 1):
                        return True
                    else:
                        groupTarget[i] += n
            return False

        return dfs(0)
        
        
# @lc code=end

if __name__ == '__main__':
    nums = [2,2,2,2,3,4,5]
    nums = [10,10,10,7,7,7,7,7,7,6,6,6]

    k = 4
    k = 3
    print(Solution().canPartitionKSubsets(nums, k))
