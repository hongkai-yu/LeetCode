#
# @lc app=leetcode id=1576 lang=python3
#
# [1576] Replace All ?'s to Avoid Consecutive Repeating Characters
#

# @lc code=start
class Solution:
    def modifyString(self, s: str) -> str:
        res = ''
        leftConstraint = ''

        def letterPicker(leftConstraint, rightConstraint):
            for c in 'abc':
                if c != leftConstraint and c != rightConstraint:
                    return c

        for i in range(len(s)):
            if s[i] != '?':
                res += s[i]
                leftConstraint = s[i]
            else:
                rightConstraint = '' if i == len(s) - 1 else s[i + 1]

                l = letterPicker(leftConstraint, rightConstraint)
                res += l
                leftConstraint = l
        return res

# @lc code=end

