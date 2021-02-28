#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def checkNode(node: TreeNode, maxDiff: List[int]) -> (int, int):
            rightMax = leftMin = rightMin = leftMax = node.val
            if node.left is not None: leftMin, leftMax = checkNode(node.left, maxDiff)
            if node.right is not None: rightMin, rightMax = checkNode(node.right, maxDiff)

            maxDiff[0] = max(maxDiff[0], abs(leftMin - node.val), abs(rightMax - node.val),
                            abs(leftMax - node.val), abs(rightMin - node.val))
            return min(node.val, leftMin, rightMin), max(node.val, rightMax, leftMax)
        
        maxDiff = [0]
        checkNode(root, maxDiff)
        return maxDiff[0]
        
# @lc code=end