#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        seenOdds = 0 # could be 0, 1, 2
        for n in arr:
            if n % 2 == 1:
                if seenOdds < 2: seenOdds += 1
                else: return True # seenOdds = 2
            else: seenOdds = 0
        return False
        
# @lc code=end

if __name__ == "__main__":
    output = Solution().threeConsecutiveOdds([1,2,34,3,4,5,7,23,12])
    print(output)
