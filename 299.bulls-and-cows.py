#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        secretDigits = [0] * 10
        guessDigits = [0] * 10

        for i in range(len(secret)):
            if secret[i] == guess[i]: bulls += 1
            else:
                secretDigits[int(secret[i])] += 1
                guessDigits[int(guess[i])] += 1
        
        for i in range(10):
            cows += min(secretDigits[i], guessDigits[i])
        
        return(str(bulls) + 'A' + str(cows) + 'B')

        
# @lc code=end

