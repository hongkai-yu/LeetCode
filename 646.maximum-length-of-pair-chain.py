#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start

class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort() 
        # print(pairs)
        # dp = [1] * len(pairs)

        # for i in reversed(range(len(pairs))):
        #     end = pairs[i][1]
        #     idx = -1 
        #     lo, hi = i + 1, len(pairs) - 1
        #     while lo <= hi:
        #         if lo == hi:
        #             if pairs[lo][0] > end:
        #                 idx = lo
        #             break

        #         mid = (lo + hi) // 2
        #         if pairs[mid][0] <= end:
        #             lo = mid + 1
        #         else:
        #             hi = mid
        #     if idx == -1:
        #         pass
        #     else:
        #         dp[i] += max(dp[idx:])
        # # print(dp)
        # return max(dp)

        first = pairs.pop()[0]
        chainLen = 1

        while pairs:
            nxtFirst, nxtSecond = pairs.pop()
            if nxtSecond < first:
                chainLen += 1
                first = nxtFirst
        return chainLen
        
        
# @lc code=end

if __name__ == '__main__':
    pairs = [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]
    print(Solution().findLongestChain(pairs))


