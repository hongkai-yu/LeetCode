#
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#

# @lc code=start
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = len)
        
        result = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        return result
        
# @lc code=end

if __name__ == '__main__':
    words = ["mass","as","hero","superhero"]
    words = ["leetcode","et","code"]
    words = ["leetcoder","leetcode","od","hamlet","am"]
    print(Solution().stringMatching(words))

