#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in reversed(range(len(ratings) - 1)):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        
        return sum(candies)
        
# @lc code=end

if __name__ == '__main__':
    ratings = [29,51,87,87,72,12]
    print(Solution().candy(ratings))
    
