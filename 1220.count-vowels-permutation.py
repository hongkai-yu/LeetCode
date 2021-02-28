#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#

# @lc code=start
from functools import lru_cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        nextVowel = {'a': {'e'},
                     'e': {'a', 'i'},
                     'i': {'a', 'e', 'o', 'u'},
                     'o': {'i', 'u'},
                     'u': {'a'}
                     }
        @lru_cache
        def endVowelDict(n: int) -> dict:
            if n == 1:
                return {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
            prevDict = endVowelDict(n - 1)
            newDict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
            for endVowel, comb in prevDict.items():
                for v in nextVowel[endVowel]:
                    newDict[v] += comb
            return newDict
        
        return sum(endVowelDict(n).values()) % (10 ** 9 + 7)

                


# @lc code=end
if __name__ == "__main__":
    print(Solution().countVowelPermutation(5))
