#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        value = root.val
        def checkBranch(node: TreeNode) -> bool:
            if node is None: return True
            else:
                if node.val != value: return False
                return checkBranch(node.left) and checkBranch(node.right)
        return checkBranch(root)
        
        
# @lc code=end

