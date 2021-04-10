#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Trsee
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),
                       self.maxDepth(root.right))
        
# @lc code=end
