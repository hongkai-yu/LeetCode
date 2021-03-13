#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # step 1
        s = s.strip()
        if s == '':
            return 0

        # step 2
        postive = True
        if s[0] in '+-':
            if s[0] == '-': postive = False
            s = s[1:]

        # step 3
        strRes = '0'
        for c in s:
            if not c.isdigit(): break
            else: strRes += c
        
        # step 4
        intRes = int(strRes) if postive else -int(strRes)

        # step 5 & 6
        return max(-2**31, min(intRes, 2**31-1))

# @lc code=end

