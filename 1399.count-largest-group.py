#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#

# @lc code=start
from collections import defaultdict
from collections import Counter
from operator import countOf


class Solution:
    def countLargestGroup(self, n: int) -> int:
        c = Counter(sum(map(int, str(i))) for i in range(1, n+1))
        return countOf(c.values(), max(c.values()))
        
        
    # def countLargestGroup(self, n: int) -> int:
    #     groups = defaultdict(set)
        
    #     for i in range(1, n + 1):
    #         s = sum([int(digit) for digit in str(i)])
    #         groups[s].add(i)
        
    #     sizes = [len(groups[s]) for s in groups]
    #     maxSize = max(sizes)
    #     return len([s for s in sizes if s == maxSize])

        
# @lc code=end

if __name__ == "__main__":
    print(Solution().countLargestGroup(13))

