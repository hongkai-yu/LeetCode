#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern): return False

        d = {}
        for letter, word in zip(pattern, words):
            if letter in d:
                if d[letter] != word: return False
            else: d[letter] = word
        return len(set(d.values())) == len(d.values())



        
# @lc code=end

