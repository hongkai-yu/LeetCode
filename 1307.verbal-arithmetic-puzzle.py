#
# @lc app=leetcode id=1307 lang=python3
#
# [1307] Verbal Arithmetic Puzzle
#

# @lc code=start
from operator import __or__
from functools import reduce
from typing import List
from itertools import permutations


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        letters = reduce(__or__, map(set, words)) | set(result)
        if len(letters) > 10:
            return False
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        firstLetter = set(word[0] for word in words) | set(result[0])

        for assign in permutations(digits, len(letters)):
            assignDict = dict(zip(letters, assign))
            if any(assignDict[l] == 0 for l in firstLetter):
                continue

            if sum(map(lambda word: self.decode(word, assignDict), words)) == self.decode(result, assignDict):
                print(assignDict)
                return True

        return False

    def decode(self, word: str, assignDict: dict) -> int:
        res = 0
        word = list(word)
        pos = 0
        while word:
            res += assignDict[word.pop()] * (10 ** pos)
            pos += 1
        return res
        
# @lc code=end

if __name__ == '__main__':
    words = ["SEND","MORE"]
    words = ["LEET","CODE"]
    words = ["SIX","SEVEN","SEVEN"]
    # words = ["THIS","IS","TOO"]

    result = "MONEY"
    result = "POINT"
    result = "TWENTY"
    # result = "FUNNY"
    print(Solution().isSolvable(words, result))

