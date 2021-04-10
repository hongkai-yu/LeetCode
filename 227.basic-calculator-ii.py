#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
import re
# from math import abs

class Solution:
    def calculate(self, s: str) -> int:

        nums = list(map(int, re.findall(r'[0-9]+', s)))
        operators = ['+'] + re.findall(r'[\+\-\*\/]', s) 


        stack = []
        for num, op in zip(nums, operators):
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            else:
                prev = stack.pop()
                if prev >= 0:
                    stack.append(abs(prev) // num)
                else:
                    stack.append(-(abs(prev) // num))
        return sum(stack)
# @lc code=end

if __name__ == "__main__":
    s = "14 - 3 / 2"
    print(Solution().calculate(s))

