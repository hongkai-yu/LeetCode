#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)): dp[i][i] = True

        maxLen = 1
        res = s[0]

        for j in range(len(s)):
            for i in range(j):
                if s[i] != s[j]: continue
                # s[i] == s[j]
                if i == j - 1 or dp[i+1][j-1]:
                    dp[i][j] = True
                    newLen = j - i + 1
                    if newLen > maxLen:
                        maxLen = newLen
                        res = s[i:j+1]
        return res


    #     return max([self.maxExpansion(s, i, i) for i in range(len(s))] +
    #                [self.maxExpansion(s, i, i + 1) for i in range(len(s) - 1)], key=len)

    # def maxExpansion(self, s: str, i: int, j: int) -> str:
    #     if s[i] != s[j]:
    #         return ''

    #     res = s[i] + s[j] if i < j else s[i]

    #     while i > 0 and j < len(s) - 1:
    #         i -= 1
    #         j += 1
    #         if s[i] != s[j]:
    #             break
    #         else:
    #             res = s[i] + res + s[j]

    #     return res

# @lc code=end

if __name__ == '__main__':
    s = 'babad'
    print(Solution().longestPalindrome(s))
