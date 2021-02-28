#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1: return True

        capitalize = [str.isupper(l) for l in word]
        
        if capitalize[0]:
            if all(not b for b in capitalize[1:]) or all(capitalize[1:]): return True
            else: return False
        else:
            if all(not b for b in capitalize[1:]): return True
            else: return False


        
        
# @lc code=end

