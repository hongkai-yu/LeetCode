#
# @lc app=leetcode id=898 lang=python3
#
# [898] Bitwise ORs of Subarrays
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        N = len(arr)

        @lru_cache(maxsize=N)
        def solutionStartWith(i: int) -> set:

            if i == N:
                return set()

            return {arr[i]} | {arr[i] | s for s in solutionStartWith(i + 1)}

        return len(set().union(*[solutionStartWith(i) for i in range(N)]))


# @lc code=end
if __name__ == "__main__":
    a = Solution().subarrayBitwiseORs([1, 2, 4])
    print(a)
