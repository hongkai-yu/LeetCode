#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        clusters = []

        curCluster = 0
        for num in nums:
            if num == 1: curCluster += 1
            else:
                clusters.append(curCluster)
                curCluster = 0
        clusters.append(curCluster)

        if len(clusters) == 1:  return max(clusters[0] - 1, 0)

        maxSize = 0
        for i in range(1, len(clusters)):
            merged = clusters[i-1] + clusters[i]
            if merged > maxSize: maxSize = merged
        
        return maxSize

        
# @lc code=end

