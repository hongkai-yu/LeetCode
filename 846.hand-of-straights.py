#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], W: int) -> bool:
        c = Counter(hand)

        for i in sorted(c):
            if c[i] > 0:
                cur = c[i]
                for j in range(W):
                    c[i + j] -= cur
                    if c[i + j] < 0:
                        return False
        return True

        

if __name__ == '__main__':
    hand = [1,2,3,6,2,3,4,7,8]
    W = 3
    print(Solution().isNStraightHand(hand, W))
        
        
# @lc code=end

