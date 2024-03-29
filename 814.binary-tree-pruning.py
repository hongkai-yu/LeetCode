#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and (not root.left) and (not root.right):
            return None
        else:
            return root
        
# @lc code=end

