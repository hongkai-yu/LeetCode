#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for c in s:
            if c in d:  d[c] += 1
            else:       d[c] = 1
        output = ''
        for c, f in sorted(d.items(), key = lambda item: item[1], reverse = True):
            output += c * f
        return output

        
# @lc code=end
if __name__ == "__main__":
    print(Solution().frequencySort('tree'))

