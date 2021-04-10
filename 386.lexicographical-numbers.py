#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # return list(map(int, sorted(map(str, range(1, n + 1)))))
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []

        def dfs(num: int) -> bool:
            if num > n:
                return False
            res.append(num)
            for d in digits:
                if not dfs(num * 10 + d):
                    continue

        for d in digits[1:]:
            dfs(d)
        return res

        
# @lc code=end

