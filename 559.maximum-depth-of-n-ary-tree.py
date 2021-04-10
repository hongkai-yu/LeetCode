#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node: 'Node', level: int = 0) -> int:
            if not node:
                return level
            elif not node.children:
                return level + 1
            else: 
                return max(dfs(child, level + 1) for child in node.children)
        return dfs(root)
        
# @lc code=end

