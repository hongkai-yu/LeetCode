#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from itertools import product 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        if len(word) > m * n:
            return False

        # visited = set()

        for i, j in product(range(m), range(n)):
            if self.dfs(i, j, board, word):
                return True
        return False

    def dfs(self, i, j, board, word):
 
        m = len(board)
        n = len(board[0])

        if word[0] != board[i][j]:
            return False

        if len(word) == 1:
            return True

        # visited.add(i * n + j)

        board[i][j], tmp = '#', board[i][j]
        # for ip, jp in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        #     if 0 <= ip < m and 0 <= jp < n 
        #         if self.dfs(ip, jp, board, word[1:]):
        #             return True
        
        if any(self.dfs(ip, jp, board, word[1:])
                for ip, jp in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                if 0 <= ip < m and 0 <= jp < n):
            return True

        # visited.remove(i * n + j)
        board[i][j] = tmp
        return False


        
# @lc code=end

