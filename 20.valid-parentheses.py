#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
from queue import deque


class Solution:
    def isValid(self, s: str) -> bool:

        correspond = {'(': ')', '[': ']', '{': '}'}
        stack = deque([])

        for c in s:
            if c in '([{': stack.append(c)
            elif c in ')]}':
                if not stack or correspond[stack.pop()] != c:
                    return False
            else:
                raise KeyError
        
        return len(stack) == 0
        
# @lc code=end

if __name__ == "__main__":
    print(Solution().isValid('([])'))
    print(Solution().isValid(']'))
    print(Solution().isValid('([)]'))

