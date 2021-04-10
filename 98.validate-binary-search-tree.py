#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from math import inf


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # low, high = -inf, inf
        low, high = -2**31 - 1, 2**31
        return self.dfs(root, low, high)

    def dfs(self, node: TreeNode, low: int, high: int) -> bool:

        if not node:
            return True

        return (low < node.val < high
                and self.dfs(node.left, low, node.val)
                and self.dfs(node.right, node.val, high))

# @lc code=end
