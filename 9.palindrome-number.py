#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x)[::-1] == str(x)
        if x < 0: return False
        digits = []
        while (x != 0 ):
            d, x = x % 10, x // 10
            digits.append(d)
        return digits == digits[::-1]

        
# @lc code=end

if __name__ == "__main__":
    print(Solution().isPalindrome(121))

