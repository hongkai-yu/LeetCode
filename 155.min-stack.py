#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
from collections import deque
from math import inf


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.minElement = inf
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minElement = min(self.minElement, x)
        
        
    def pop(self) -> None:
        self.stack.pop()
        self.minElement = min(self.stack) if self.stack else inf
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minElement
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

