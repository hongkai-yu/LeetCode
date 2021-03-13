#
# @lc app=leetcode id=1175 lang=python3
#
# [1175] Prime Arrangements
#

# @lc code=start
import math

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        nPrime = len([i for i in range(1, n+1) if self.isPrime(i)])
        return (math.factorial(nPrime) * math.factorial(n - nPrime)) % (10**9 + 7)

    def isPrime(self, n: int) -> bool:
        if n == 1: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

# @lc code=end

if __name__ == '__main__':
    print(Solution().numPrimeArrangements(5))
    print(Solution().numPrimeArrangements(100))