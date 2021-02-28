#
# @lc app=leetcode id=1432 lang=python3
#
# [1432] Max Difference You Can Get From Changing an Integer
#

# @lc code=start
class Solution:
    def maxDiff(self, num: int) -> int:
        digits = str(num)

        swapDigit = ''
        for digit in digits:
            if digit != '9':
                swapDigit = digit
                break
        maxNum = int(digits.replace(swapDigit, '9')) if swapDigit else num
        
        swapDigit = ''
        if digits[0] != '1':
            swapDigit = digits[0]
            minNum = int(digits.replace(swapDigit, '1'))
        else:
            for digit in digits[1:]:
                if digit != '0' and digit != '1':
                    swapDigit = digit
                    break
            minNum = int(digits.replace(swapDigit, '0')) if swapDigit else num

        # print(maxNum, minNum)
        return maxNum - minNum
# @lc code=end

if __name__ == "__main__":
    print(Solution().maxDiff(123456))
    print(Solution().maxDiff(9))
    print(Solution().maxDiff(10000))
    print(Solution().maxDiff(111))

