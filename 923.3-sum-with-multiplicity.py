#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#

# @lc code=start
from typing import List
from collections import Counter
from itertools import combinations_with_replacement


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:


        res = 0
        # arr.sort()

        c = Counter(arr)

        for i, j in combinations_with_replacement(c, 2):
            k = target - i - j
            i, j = min(i, j), max(i, j)
            if i == j == k: res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
            elif i == j != k: res += c[i] * (c[i] - 1) // 2 * c[k]
            elif i < j < k: res += c[i] * c[j] * c[k]

        # arr.sort()
        # for i in range(len(arr)):
        #     j, k = i + 1, len(arr) - 
        #     while j < k:
        #         s = arr[i] + arr[j] + arr[k]
        #         if s < target:
        #             j += 1
        #         elif s > target:
        #             k -= 1
        #         else: # s == target
        #             # print(arr[i], arr[j], arr[k], res)
        #             if arr[j] == arr[k]:
        #                 res += (k - j + 1) * (k - j) // 2
        #                 break
        #             else:
        #                 sameJ = 1
        #                 while arr[j + 1] == arr[j]:
        #                     j += 1
        #                     sameJ += 1 
        #                 j += 1

        #                 sameK = 1
        #                 while arr[k - 1] == arr[k]:
        #                     k -= 1
        #                     sameK += 1
        #                 k -= 1
        #                 res += sameJ * sameK
        return res % (10 ** 9 + 7)
# @lc code=end

if __name__ == '__main__':
    arr = [2, 1, 3]

    print(Solution().threeSumMulti(arr, 6))

