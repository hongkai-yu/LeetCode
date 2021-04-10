#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        substring = {s[0] : 0}

        maxLen = 1
        i = 0
        for j in range(1, len(s)):
            if s[j] not in substring or i > substring[s[j]]:
                maxLen = max(maxLen, j - i + 1)
            else:
                i = substring[s[j]] + 1
            substring[s[j]] = j

        return maxLen
            
        
# @lc code=end

