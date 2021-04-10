#
# @lc app=leetcode id=1157 lang=python3
#
# [1157] Online Majority Element In Subarray
#

# @lc code=start
from collections import Counter
from functools import cache


class MajorityChecker:

    def __init__(self, arr: List[int]):
        # self.arr = arr

        

    def query(self, left: int, right: int, threshold: int) -> int:
        num, freq = self.mostCommon(left, right)
        if freq >= threshold:
            return num
        else:
            return -1

    # @cache
    def mostCommon(self, left, right) -> (int, int):
        # c = Counter(self.arr[left: right + 1])
        # return c.most_common(1)[0]

    # def findMajority()

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# @lc code=end

