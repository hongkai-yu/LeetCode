#
# @lc app=leetcode id=1577 lang=python3
#
# [1577] Number of Ways Where Square of Number Is Equal to Product of Two Numbers
#

# @lc code=start
from collections import Counter


class Solution:
    def numTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)

        def numOneWay(c1: Counter, c2: Counter) -> int:
            res = 0
            for ni in c1:
                ni2 = ni * ni
                for nj in c2:
                    nk, mod = divmod(ni2, nj)
                    if mod != 0:
                        continue

                    if nj < nk:
                        res += c1[ni] * c2[nj] * c2[nk]
                    elif nj == nk:
                        res += c1[ni] * c2[nj] * (c2[nj] - 1) // 2
                    else:
                        pass
            return res

        return numOneWay(nums1, nums2) + numOneWay(nums2, nums1)


# @lc code=end

if __name__ == '__main__':
    nums1 = [4,7,9,11,23]
    nums2 = [3,5,1024,12,18]

    nums1 = [1,1]
    nums2 = [1,1,1] 

    nums1 = [7,7,8,3]
    nums2 = [1,2,9,7]    
    print(Solution().numTriplets(nums1, nums2))

