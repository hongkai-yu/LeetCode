#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        process = set()
        while(True):
            process.add(n)
            n = sum(int(i)**2 for i in str(n))
            if n == 1: return True
            elif n in process: return False

        
# @lc code=end

