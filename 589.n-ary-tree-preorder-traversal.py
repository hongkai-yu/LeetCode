#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
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
    def preorder(self, root: 'Node') -> List[int]:
        order = []
        def dfs(node: 'Node', order: list[int]) -> None:
            if node is None: return
            order.append(node.val)
            for node in node.children: dfs(node, order)
        dfs(root, order)
        return order
        
# @lc code=end

