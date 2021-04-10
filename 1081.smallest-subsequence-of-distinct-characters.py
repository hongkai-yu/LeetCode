#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#

# @lc code=start

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack = []

        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and c < stack[-1] and i < last[stack[-1]]:
                # smaller and stack[-1] exists
                stack.pop()
            stack.append(c)
        return ''.join(stack)
        
# @lc code=end

