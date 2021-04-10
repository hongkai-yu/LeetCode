#
# @lc app=leetcode id=781 lang=python3
#
# [781] Rabbits in Forest
#

from collections import Counter


# @lc code=start
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)

        res = 0
        for ans, freq in c.items():
            numOfCol = 1
            while numOfCol * (ans + 1) < freq:
                numOfCol += 1
            res += numOfCol * (ans + 1)
            # res += ((freq // (ans + 1)) + 1) * (ans + 1)
        return res
            
        
# @lc code=end

