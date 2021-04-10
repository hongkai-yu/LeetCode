#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        else:
            if haystack[:len(needle)] == needle:
                return 0
            else:
                nextStr = self.strStr(haystack[1:], needle)
                return 1 + nextStr if nextStr >= 0 else -1 
        
# @lc code=end

