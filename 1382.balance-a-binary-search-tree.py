#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        orderedVals = []

        def dfs(node: TreeNode) -> None:
            if not node: return 

            dfs(node.left)
            orderedVals.append(node.val)
            dfs(node.right)
        
        def buildTree(l: int, r: int) -> TreeNode:
            if l == r: return None

            mid = (r + l) // 2
            return TreeNode(orderedVals[mid], buildTree(l, mid), buildTree(mid+1, r))
        
        dfs(root)
        return buildTree(0, len(orderedVals))

        
# @lc code=end

