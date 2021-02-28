#
# @lc app=leetcode id=1390 lang=python3
#
# [1390] Four Divisors
#

# @lc code=start
from math import sqrt, ceil


class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:

        def getDivisorsSumIfFour(num: int) -> int:
            assert num >= 1

            divisors = set()
            for i in range(1, ceil(sqrt(num)) + 1):
                if num % i == 0: 
                    divisors.add(i)
                    divisors.add(num // i)
                    if len(divisors) > 4: return 0

            if len(divisors) == 4: return sum(divisors)
            else:                  return 0

        return sum(map(getDivisorsSumIfFour, nums))
# @lc code=end
